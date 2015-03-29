__author__ = 'Stuart'

import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.openid import OpenID
from flask.ext.login import LoginManager
from flask.ext.mail import Mail
from flask.ext.babel import Babel, lazy_gettext
from flask.json import JSONEncoder
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
from .momentjs import momentjs

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
mail = Mail(app)
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app,os.path.join(basedir,'tmp'))
lm.login_view = 'login' # tells Flask-Login which view logs users in
lm.login_message = lazy_gettext("Please log in to access this page")
app.jinja_env.globals['momentjs'] = momentjs  # exposes class as a global variable available to all templates
babel = Babel(app)

class CustomJSONEncoder(JSONEncoder):
    """This class adds support for lazy translation texts to Flask's JSON encoder. This is necessary when
    flashing translated texts."""
    def default(self,obj):
        from speaklater import is_lazy_string
        if is_lazy_string(obj):
            try:
                return unicode(obj)  # python2
            except NameError:
                return str(obj)  # python3
        return super(CustomJSONEncoder,self).default(obj)

app.json_encoder = CustomJSONEncoder

if not app.debug:  # only do this part if we aren't in debug mode, otherwise data just gets dumped in browser like norm
    # python -m smtpd -n -c DebuggingServer localhost:25 starts local email server
    # https://docs.python.org/3.4/library/logging.html
    import logging
    from logging.handlers import SMTPHandler  # for email logging
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER,MAIL_PORT), 'no-reply@'+MAIL_SERVER, ADMINS, 'microblog failure', credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

    from logging.handlers import RotatingFileHandler  # for file logging
    file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)  # goes to temp directory.
        # size limited to 1 mb, keep last 10 log files as backups
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s: %(lineno)d]'))
        # info formatted. Timestamp, logging level, file & lineno where message originated, in addition to stact trace
    app.logger.setLevel(logging.INFO)  # app logger and file logger, set lower to information level, so we get more
    file_handler.setLevel(logging.INFO)  # useful messages. Every time we start without bugging, there will be a log
    app.logger.addHandler(file_handler)  # debugging web server that is online and in use very hard, log to file useful
    app.logger.info('microblog startup')


from app import views,models
# this is at the end to avoid circular imports, since views module imports app variable defined in this script.