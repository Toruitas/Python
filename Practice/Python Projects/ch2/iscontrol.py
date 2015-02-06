__author__ = 'Stuart'

"""
http://www.theasciicode.com.ar/
http://stackoverflow.com/questions/5891453/is-there-a-python-library-that-contains-a-list-of-all-the-ascii-characters

"""

from ctypes import cdll
libc = cdll.msvcrt

def is_control():
    chars = [chr(i) for i in range(128)]
    print(chars)
    for c in chars:
        ctrl = libc.iscntrl(c)
        print("{} is a control character: {}".format(c, ctrl))

def is_control_2():
    """
    Since all the control characters are invisible, it's better to not use chr to translate them.
    Must use the ascii code pointer
    :return:
    """
    for c in range(128):
        print("{} is a control character".format(c) if libc.iscntrl(c) else "{} is not a control character".format(c))

is_control_2()
