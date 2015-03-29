__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/shp28/4192012_challenge_41_easy/

Write a program that will accept a sentence as input and then output that sentence surrounded by some type of an ASCII
decoration banner.

Sample run:
Enter a sentence: So long and thanks for all the fish
Output
*****************************************
*                                       *
*  So long and thanks for all the fish  *
*                                       *
*****************************************
Bonus: If the sentence is too long, move words to the next line.

"""

def banner(string, length=25):
    print("*"*length)
    print("*"+" "*(length-2)+"*")
    while string:
        if len(string)>(length-6):
            print("*  " + string[:length-6] + "  *")
            string = string[length-6:]
        else:
            print("*  {:^{len}}  *".format(string, len=(length-6)))  # formatting codes come after the : ^ means center
            break
    print("*"+" "*(length-2)+"*")
    print("*"*length)

def banner2(string, length):
    import textwrap

    max_len = length - 6
    wrapped_text = textwrap.wrap(string,max_len)

    print("*"*length)
    print("*"+" "*(length-2)+"*")
    for line in wrapped_text:
        print("*  {}  *".format(line.center(max_len)))
    print("*"+" "*(length-2)+"*")
    print("*"*length)

def wrapped_text(string):
    """
    https://docs.python.org/3.4/library/textwrap.html
    :param string:
    :return:
    """
    import textwrap

    wrapped_text = textwrap.wrap(string, 76)
    max_line_length = max(len(line) for line in wrapped_text)
    full_line_length = max_line_length + 4

    print('*' * full_line_length)
    for line in wrapped_text:
        print('* {0} *'.format(line.center(max_line_length)))
    print('*' * full_line_length)

print(banner2("So long and thanks for all the fish",25))