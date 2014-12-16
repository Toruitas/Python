__author__ = 'Stuart'

#this one is like your scripts with argv
def print_two(*args):
    arg1,arg2 = args
    print("arg1: {}, arg2: {}".format(arg1,arg2))

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print("arg1: {}, arg2: {}".format(arg1,arg2))

#this one takes only 1 arg
def print_one(arg1):
    print("arg1: {}".format(arg1))

#this one takes no args
def print_none():
    print("I got nothin'.")

print_two("Stuart","Leitch")
print_two_again("Stuart","Leitch")
print_one("First!")
print_none()