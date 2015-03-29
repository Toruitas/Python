__author__ = 'Stuart'
#!flask/bin/python

import os
import sys

if sys.platform == 'win32':
    pybabel = 'flask\\scripts\\pybabel'
else:
    pybabel = 'flask/bin/pybabel'

os.system(pybabel + ' compile -d app/translations')