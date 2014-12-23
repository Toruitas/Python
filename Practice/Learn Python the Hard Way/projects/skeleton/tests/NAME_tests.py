__author__ = 'Stuart'

from nose.tools import *
import sys

# print(sys.path)
sys.path.insert(0,"C:\\Users\\Stuart\\Documents\\GitHub\\Python\\Practice\\Learn Python the Hard Way\\projects\\skeleton")
# this adds the skeleton directory to sys.path so we can get to NAME...
# there may be a better way?
# print(sys.path)
import NAME

def setup():
    print("SETUP!")

def teardown():
    print("TEARDOWN!")

def test_basic():
    print("I RAN!")