__author__ = 'Stuart'

from flask.ext.mail import Message
from flask import render_template
from app import mail, app
from config import ADMINS
# from threading import Thread
from .decorators import async


def send_email(subject, sender, recipients, text_body, html_body):
    """
    Sends an email
    flask mail goes beyond this, with bcc, and attachments too
    :param subject:
    :param sender:
    :param recipients:
    :param text_body:
    :param html_body:
    :return:
    """
    msg = Message(subject, sender=sender, recipients = recipients)
    msg.body = text_body
    msg.html = html_body
    # thr = Thread(target=send_async_email, args=[app,msg])  # creates separate thread for sending an email
    # thr.start()
    send_async_email(app,msg)

@async
def send_async_email(app, msg):
    """
    starts a new process sending Message object with args.
    since is separate thread, need to set context manually. Flask-mail's app context won't be automatic.
    By using the @async decorator, we get to refer to one function that will automatically be threaded.
    :param app:
    :param msg:
    :return:
    """
    with app.app_context():
        mail.send(msg)

def follower_notification(followed, follower):
    """
    Creates an email based off render_template, and sends it to send_email for sending a follower notification.
    sends notification email to someone that they are being followed.
    Keeping logic separate from presentation, emails also go into template folder along with views.
    :param followed:
    :param follower:
    :return:
    """
    send_email("[microblog {} is now following you!".format(follower.nickname),
               ADMINS[0],
               [followed.email],
               render_template("follower_email.txt",
                               user=followed, follower=follower),
               render_template("follower_email.html",
                               user=followed, follower=follower))

