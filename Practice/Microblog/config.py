__author__ = 'Stuart'
# -*- coding: utf-8 -*-

# since Español has a special letter, we add the coding comment to tell interpreter we are using UTF-8 not ASCII, which
# doesn't have ñ character

WTF_CSRF_ENABLED = True  # cross-site request forgery prevention
SECRET_KEY = 'youwillneverguess'  # only when CSRF enabled, creates crypto token to validate. Use a harder one.

OPENID_PROVIDERS =[
    {'name':'Google', 'url':'https://www.google.com/accounts/o8/id', 'img':'/static/image/google.png'},
    {'name':'Yahoo', 'url':'https://me.yahoo.com', 'img':'/static/image/yahoo.png'},
    {'name':'AOL', 'url':'https:openid.aol.com/<username>','img':'/static/image/aol.png'},
    {'name':'Flickr', 'url':'https://flickr.com/<username>', 'img':'/static/image/flickr.png'},
    {'name':'MyOpenID', 'url':'https://www.myopenid.com', 'img':'/static/image/myopenid.png'}
]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')  # required by Flask-sqlalchemy extension
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')  # folder where we store SQLalchemy-migrate files

# mail server settings
# need: email server used to send emails, plus any authentication; email addy(s) of admins
# username/password should be environment variables set locally, not hardcoded in a source file - may accidentally
# get uploaded to github!
# http://www.reddit.com/r/flask/comments/2v5j2y/question_about_osenvironget_when_using_flaskmail/  for how to set
# mail_username and password
# hint: set MAIL_USERNAME="username" has to be in double quotes
# set MAIL_PASSWORD = "password"
# $env:MyTestVariable = "My temporary test variable."
MAIL_SERVER = 'smtp.gmail.com'  # localhost your.mailserver.com
MAIL_PORT = 465 #25
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  #
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['toruitas@gmail.com']

# pagination. It's good to have these global 'knobs' that can change behavior of app in config file all at once.
POSTS_PER_PAGE = 3

# name of full text search db
WHOOSH_BASE = os.path.join(basedir,'search.db')
MAX_SEARCH_RESULTS = 50

# available languages
# has keys for available languages, and printable value for that name. Using short codes here, but could easily do
# en-US and en-GB etc etc.
LANGUAGES = {
    'en':'English',
    'es':'Español'
}

#microsoft translation service
MS_TRANSLATOR_CLIENT_ID = 'ToruitasFlaskTestMicroblog'
MS_TRANSLATOR_CLIENT_SECRET = "Gwxt6YdkKIDh5WHNnSeNBCezyVWISgMkJzBa4NTGvYQ="