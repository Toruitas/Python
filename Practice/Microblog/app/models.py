__author__ = 'Stuart'

"""
Remember, every time you modify the Columns of any table (i.e. adding about_me to User), you must migrate it.
"""

from app import db, app
from hashlib import md5
import re

enable_search = True
import flask.ext.whooshalchemy as whooshalchemy




followers = db.Table('followers',
                     db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('followed_id', db.Integer, db.ForeignKey('user.id')))
# not a model. Since is aux table, no data other than foreign keys, use lower level APIs in Flask-SQLAlchemy to create
# without a model.

class User(db.Model):  # model for User table
    id=db.Column(db.Integer,primary_key=True)
    nickname = db.Column(db.String(64),index=True,unique=True)  # 64 is the max length
    email = db.Column(db.String(120),index=True,unique=True)
    posts = db.relationship('Post',backref='author',lazy='dynamic')
    # this (relationship) field normally defined on the 'one' side of 1-many
    # first arg indicates "many" class of this relationship - the Post class
    # backref defines a field that will be added to objects of 'many' class that points back at 'one' object
    # in this case - post.author gets User instance that create the post
    # Think of it as a possessive. It will populate the ID for posts, and post ids for user.
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)
    followed = db.relationship('User',
                               secondary = followers,
                               primaryjoin = (followers.c.follower_id == id),
                               secondaryjoin = (followers.c.followed_id == id),
                               backref = db.backref('followers', lazy = 'dynamic'),
                               lazy = 'dynamic')
    # first, link User instances to User instances. Left side following right side. So
    # From perspective of left User, so variable named followed...
    # 'User' is the right side Class. Self referential relationship, so same class. Left side is parent class.
    # secondary: association table used for relationship
    # primaryjoin: condition that links left side (the follower) with assoc table. Since followers isn't a model,
    #   syntax is a bit weird.
    # secondaryjoin: condition linking right side entity (the followed) with assoc table
    # backref: how relationship accessed from right side. For a given user, query named 'followed' returns all rights
    #   that have target user on left side. Backref called followers and returns all lefts linked to target in right
    #   side. 'lazy' indicates execution mode for query. 'dynamic' won't set query to run unless requested. This way
    #   we have performance gains, and can modify the query before it executes.
    # lazy: like above, but applies to regular query, not backref query.

    def is_authenticated(self):
        """
        :return: True unless obj represents user that shouldn't be allowed to authenticate.
        """
        return True

    def is_active(self):
        """
        :return: True for users unless they are inactive - like if they were banned
        """
        return True

    def is_anonymous(self):
        """
        :return: True only for fake users not supposed to log in to the system
        """
        return False

    def get_id(self):
        """
        :return: unique ID for user.
        """
        # try:
        #     return unicode(self.id)
        # except NameError:
        return str(self.id)

    def avatar(self, size):
        """
        just need to create md5 hash of the user email and incorp into URL
        d=mm determines what placeholder image is returned when user has no Gravatar acct. mm option returns mysteryman
        s=N requests image scaled to given size in pixels
        https://en.gravatar.com/site/implement/images
        :param size: size in pixels. Avatar will be square. So this is just one dimension.
        :return: picture from gravatar, scaled to size
        """
        return 'http://www.gravatar.com/avatar/{}?d=mm&s={}'.format(md5(self.email.encode('utf-8')).hexdigest(),size)

    def follow(self,user):
        """
        http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers-contacts-and-friends
        :param user: user to follow
        :return: object if success, None otherwise
        """
        if not self.is_following(user):
            self.followed.append(user)
            return self

    def unfollow(self, user):
        """
        TO BLOCK USERS, SEE COMMENTS OF ABOVE LINK
        :param user:
        :return:
        """
        if self.is_following(user):
            self.followed.remove(user)
            return self

    def is_following(self, user):
        """
        Takes followed query, which returns all the (follower, followed) pairs that have our user as follower, and
        filter it by followed user. Possible, since followed's lazy='dynamic' so this is the actual query obj, not
        the result of the query
        db.c(olumn).nameofcolumn
        :param user: our user
        :return: existence of link (if greater than 0, exists, else doesn't)
        """
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        """
        Join called on post table. args(other table-followers table, join condition). Creates temp new table with data
        from Post and followers. Merged according to condition.
        We want followed_id of followers table to match user_id field of Post table.
        Take each record from Post table (left side of join) and append fields from records in 'followers' table that
        match condition.
        If no match, that post record is not included.

        Then, we filter this according to id to only show posts followed by the User.

        The order_by line sorts it with most recent first.

        To see own posts, just add User as follower of self.
        :return:
        """
        return Post.query.join(followers,(followers.c.followed_id == Post.user_id)).filter(
            followers.c.follower_id == self.id).order_by(Post.timestamp.desc())

    def sorted_posts(self):
        return self.posts.order_by(Post.timestamp.desc())

    @staticmethod
    def make_unique_nickname(nickname):
        """
        Simply adds a counter to requested nickname until unique name is found.
        Static method since operation doesn't apply to any particular instance of the class.
        :param nickname:
        :return:
        """
        if User.query.filter_by(nickname=nickname).first() is None:
            return nickname
        version = 2
        while True:
            new_nickname = nickname +str(version)
            if User.query.filter_by(nickname=new_nickname).first() is None:
                break
            version +=1
        return new_nickname

    @staticmethod
    def make_valid_nickname(nickname):
        """
        To prevent malicious nicknames, remove anything that isn't a letter, number, dot, or underscore
        :param nickname: submitted method
        :return: fixed nick
        """
        return re.sub('[^a-zA-Z0-9_\.]','',nickname)

    def __repr__(self):
        return '<User {}>'.format(self.nickname)

class Post(db.Model):  # model for Posts table
    __searchable__ = ['body']
    # array with all the db fields that will be in searchable index. This time, only post bodies

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    language = db.Column(db.String(5))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

if enable_search:
    whooshalchemy.whoosh_index(app,Post)