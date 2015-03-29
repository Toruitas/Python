__author__ = 'Stuart'
# writes config file

import configparser

config = configparser.ConfigParser()
config['EMAIL'] = {'SEND_FROM' : 'notlogging@yahoo.com',
                   'SEND_TO':'notlogging@yahoo.com',
                   'USERNAME' : 'notlogging',
                   'PASSWORD' : 'Se@ttle$',
                   'SERVER' : 'smtp.mail.yahoo.com',
                   'PORT' : '465'}
config['FTP'] = {'FTP_USER':'test','FTP_PASSWORD' : '',
                 'FTP_SERVER' : '192.168.0.101',
                 'FTP_PORT' : '37994'}
with open('config1.ini','w') as configfile:
    config.write(configfile)