__author__ = 'Stuart'
"""
Web forms are represented in Flask-WTF as classes, subclassed from base class Form.
A form subclass simply defines the fields of the form as class variables.
"""

from flask.ext.wtf import Form
from flask.ext.babel import gettext
from wtforms import StringField, BooleanField, TextAreaField  # field classes we need for this
from wtforms.validators import DataRequired, Length
from app.models import User
# validator that can be att'd to a field to validate data. This one just checks emptiness.

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class EditForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators = [Length(min=0,max=140)])

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):  # if normal validation fails, return False
            return False
        if self.nickname.data == self.original_nickname:  # if same nickname as before - no change, pass
            return True
        if self.nickname != User.make_valid_nickname(self.nickname.data):  # if nickname uses bad characters
            self.nickname.errors.append(gettext('This nickname has invalid characters. Please use letters, numbers,'
                                                'periods, and underscores only.'))
            return False
        user = User.query.filter_by(nickname = self.nickname.data).first()  # gets user
        if user != None:  # if user with that nickname exists in db, returns False
            self.nickname.errors.append(gettext('This nickname is already in use. Please choose another one.'))
            return False
        return True

class PostForm(Form):
    post = StringField('post', validators=[DataRequired()])

class SearchForm(Form):
    search = StringField('search',validators = [DataRequired()])
