__author__ = 'Stuart'
from app import app, db, lm, oid, babel
from flask import render_template, flash, redirect, session, url_for, request, g, jsonify  # templates use Jinja2 templating engine
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext.babel import gettext
from .forms import LoginForm, EditForm, PostForm, SearchForm
from .models import User, Post
from .emails import follower_notification
from datetime import datetime
from config import POSTS_PER_PAGE, MAX_SEARCH_RESULTS, LANGUAGES
from guess_language import guessLanguage
from .translate import microsoft_translate

@app.route('/', methods = ['GET','POST'])  # now we accept POST, since we want user input
@app.route('/index', methods = ['GET','POST'])
@app.route('/index/<int:page>', methods=['GET','POST'])  # page number
@login_required  # only seen by logged in users
def index(page=1):
    # user = g.user  # pass g.user to template, not fake user
    form = PostForm()
    if form.validate_on_submit():  # if the form is submitted, insert new Post record into db.
        language = guessLanguage(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''  # empty string signals unknown lang
        post = Post(body = form.post.data,
                    timestamp = datetime.utcnow(),
                    author=g.user,
                    language = language)
        db.session.add(post)
        db.session.commit()
        flash("Your post is now live!")
        return redirect(url_for('index'))
    #  could have skipped the redirect and allowed funct to continue down into rendering. So why redir?
    #  If user hits refresh, browser would resend last issued request - resulting in a double post.
    #  redir forces browser to issue another request after submision, so get the home page, not resubmit.

    #posts = g.user.followed_posts().all()  # returns sqlalch query obj, config'd to grab posts we are interested in.
    #  .all() puts all the posts into a list
    posts = g.user.followed_posts().paginate(page,POSTS_PER_PAGE,False)
    # paginate(starting page #, num items/page, error flag).items attribute of pagination obj is a list of items

    return render_template('index.html',
                           title="Home",
                           form=form,
                           posts=posts)

@app.route('/login',methods = ['GET','POST'])  # this tells Flask that this view funct accepts Get and Post
# without this, it would only accept GET, but we want to receive POST for user data.
@oid.loginhandler  # tells flask-openid this is our login view func
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
            # so that already logged in user will not have to relog
            # will redirect to Flask-built URL. http://flask.pocoo.org/docs/0.10/quickstart/#url-building
            # g global used by flask as a place to store and share data during life of a request
    form = LoginForm()
    if form.validate_on_submit():  # when called on a submission request, gathers data, runs validators, returns T/F
         ## flash('Login requested for OpenID="{}", remember_me={}'.format(form.openid.data,str(form.remember_me.data)))
           # shows a quick message on teh next page for user(or me)
                # extremely useful on production servers to provide feedback to the user regarding an action.
        session['remember_me'] = form.remember_me.data
         # similar to flask.g, flask.session stored data will be available during that request and any future request
         # made by the same client. Stays there until explicitly removed. So, Flask keeps separate session container
         # for each client of our application
        return oid.try_login(form.openid.data,ask_for=['nickname','email'])
         # triggers userauth thru OID. args:(oid from web form, list of data items we want from OID provider)
         # since User class defined nickname and email, that's what we ask for.
         # OID auth is asynchronous. Flask-oid will call function registered with oid.after_login if success, else
         # else return to login page
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers = app.config['OPENID_PROVIDERS'])

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@oid.after_login
def after_login(resp):
    """
    Called after user logs in successfully
    Validates an email
    Creates user instance if does not exist

    :param resp: Contains info returned by OpenID provider
    :return: redirect
    """
    if resp.email is None or resp.email =='':
        flash(gettext('Invalid login. Please try again.'))
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()  # looks to see if a user by that name exists
    if user is None:  # if doesn't exist
        nickname = resp.nickname
        if nickname is None or nickname == '':
            nickname = resp.email.split("@")[0]
        nickname = User.make_valid_nickname(nickname)  # removes any unauthorized characters
        nickname = User.make_unique_nickname(nickname)  # makes it unique
        user = User(nickname=nickname,email=resp.email)  # creates user
        db.session.add(user)  # adds user to DB
        db.session.commit()  # have to commit first before can add user.follow(user)
        db.session.add(user.follow(user))  # follow self, so can see own posts.
        db.session.commit()
    remember_me = False  # sets to False first
    if 'remember_me' in session:  # unless the setting is in Flask session
        remember_me = session['remember_me']  # reassign variable to whatever setting that is
        session.pop('remember_me',None)  # removes cookie with key named 'remember_me'
    login_user(user,remember = remember_me)  # restores cookie with key 'remember_me'
    return redirect(request.args.get('next') or url_for('index'))  # next page if another page was requested, or index
        # use navs to page that req's login, but aren't yet. Can protect views against non-logged in users with
        # "login_required" decorator. User will be redir'd to login page automatically, storing orig URL as next.
        # then we have to return user to that page, with the above line and some stuff in app's module __init__.py

@app.before_request
def before_request():
    """
    current_user global set by Flask-Login, so we just put a copy in g object for better access.
    With this, all requests will have access to logged in user. Even inside templates.
    :return:
    """
    g.user = current_user
    if g.user.is_authenticated():
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)  # Guess this will add user to session
        db.session.commit()  # then this will update db's user info?
        g.search_form = SearchForm()  # only create search form if user is authenticated - don't show content to others
    g.locale = get_locale() # adds browser's locale to g


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<nickname>')  # nickname is an argument, added to view function.
@app.route('/user/<nickname>/<int:page>')  # page number
@login_required
def user(nickname, page=1):
    user = User.query.filter_by(nickname=nickname).first()  # try to load user from DB
    if user == None:
        flash('User {} not found.'.format(nickname))
        return redirect(url_for('index'))
    posts = user.sorted_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('user.html',
                           user=user,
                           posts=posts)

@app.route('/edit', methods=['Get','Post'])
@login_required
def edit():
    form = EditForm(g.user.nickname)  # creates form object
    if form.validate_on_submit():  # updates stuff
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('user',nickname=g.user.nickname))  # I made this change! redirs to prof page
    else:  # refills data with original data
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit.html', form = form)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.route('/follow/<nickname>')
@login_required
def follow(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash('User {} not found.'.format(nickname))
        return redirect(url_for('index'))
    if user == g.user:
        flash("You can't follow yourself!")
        return redirect(url_for('user', nickname=nickname))
    u = g.user.follow(user)
    if u is None:
        flash("Cannot follow " + nickname + ".")
        return redirect(url_for('user', nickname = nickname))
    db.session.add(u)
    db.session.commit()
    flash("You are now following " + nickname + "!")
    follower_notification(user,g.user)
    return redirect(url_for('user', nickname = nickname))

@app.route('/unfollow/<nickname>')
@login_required
def unfollow(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash("User {} not found.".format(nickname))
        return redirect(url_for('index'))
    if user == g.user:
        flash("You can't unfollow yourself!")
        return redirect(url_for("user",nickname=nickname))
    u = g.user.unfollow(user)
    if u is None:
        flash("Cannot unfollow " + nickname + '.')
        return redirect(url_for("user",nickname=nickname))
    db.session.add(u)
    db.session.commit()
    flash("You have stopped following " + nickname + ".")
    return redirect(url_for("user",nickname = nickname))

@app.route('/search',methods=['POST'])
@login_required
def search():
    if not g.search_form.validate_on_submit():
        return redirect(url_for('index'))
    return redirect(url_for('search_results', query=g.search_form.search.data))

@app.route('/search_results/<query>')
@login_required
def search_results(query):
    results = Post.query.whoosh_search(query,MAX_SEARCH_RESULTS).all()
    return render_template('search_results.html',
                           query=query,
                           results=results)

@babel.localeselector
def get_locale():
    """
    the function targeted by this selector above will be called before each request, to give us a chance to choose the
    language when producing its response.
    For now we will do something simple, we will just read the Accept-Lanugages header sent by the browser in the HTTP
    request and find the best-matching language from the list we support. This is simple, 'best_match' method does it
    for us.

    Accept-Languages header in most browsers is config'd by default with language selected at OS level, but all give
    users chance to select others. Users can provide a list of languages, each with a weight. Looks like:
    Accept-Language: da, en-gb;q=0.8, en;q=0.7
    Danish default weight=1 is preferred, followed by GB-English, finally with generic english.

    To translate text, use gettext(string to translate) within Python code, or {{ _('string')}} inside HTML
    :return:
    """
    #return 'es'
    return request.accept_languages.best_match(LANGUAGES.keys())  # temp set to spanish for testing

@app.route('/translate', methods=['POST'])
@login_required
def translate():
    return jsonify({
        'text':microsoft_translate(request.form['text'],
                                   request.form['sourceLang'],
                                   request.form['destLang'])
    })

@app.route('/delete/<int:id>')
@login_required
def delete(id):
    post = Post.query.get(id)
    if post is None:
        flash('Post not found.')
        return redirect(url_for('index'))
    if post.author.id != g.user.id:
        flash('You cannot delete this post.')
        return redirect(url_for('index'))
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted.')
    return redirect(url_for('index'))