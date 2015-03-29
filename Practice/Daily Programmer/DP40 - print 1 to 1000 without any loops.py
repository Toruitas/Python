__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/schtf/4162012_challenge_40_easy/

Print the numbers from 1 to 1000 without using any loop or conditional statements.
Don’t just write the printf() or count statement 1000 times.
Be creative and try to find the most efficient way!
"""

def print_without_loop(n):
    """
    doesn't work, since default recursion limit in python is 1000
    :param n:
    :return:
    """
    return n + print_without_loop(n+1)

def clever():
    i = 1
    s = "print(i); i += 1;"
    exec(s*1000)  # exec executes a string as code, unless there is a syntax error.
    # The ; allows you to print multiple stuff on same line.

def clever2():
    MAX_INT = 10

    def p(x):
        print(x)

    def f(x, y):
        (y - x) and (p(x) or f(x+1, y))  # y-x == 0 would be False, so this is a workaround conditional.
        # the second part first evaluates p(x) then does the second half.


    f(1, MAX_INT+1)

def test():
    def p():
        print('green')

    def g():
        print('blue')

    def f():
        p() or g()

    f()

test()