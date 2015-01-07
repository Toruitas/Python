__author__ = 'Stuart'

def straight_line(gradient, x, constant):
    """
    returns y coordinate of a straight line:
    gradient * x + constant
    y = mx+c
    :param gradient: slope
    :param x: duh
    :param constant: y intercept
    :return:
    """
    return gradient * x + constant

# print(straight_line(2,4,-3))
#
# for x in range(10):
#     print(x,straight_line(2,x,-3))
#
# help(straight_line)

def odds(start=1):
    '''
    'yield' is like a return call that freezes in place until the next time you call it.
    Each time you reach yield, the function exits, returning the value of start at the time.
    Next time function is called, execution continues from that point.

    Generator functions become iterators so can use them in for loops.

    They are like a list but better at memory

    return all odd numbers from start upwards
    :param start: place to start from
    :return:
    '''
    if int(start) % 2 == 0:
        start = int(start) + 1
    while True:
        yield start
        start += 2

# for n in odds():
#     if n > 7:
#         break
#     else:
#         print(n)

strait_line = lambda m,x,c: m*x + c
print(strait_line(2,4,-3))

class MyClass(object):
    instance_count = 0

    def __init__(self,value):
        self.__value = value
        MyClass.instance_count += 1
        print("instance No {} created.".format(MyClass.instance_count))

    def aMethod(self,aValue):
        self.__value *= aValue

    def __str__(self):
        return "A MyClass instance with value: " + str(self.__value)

    def __del__(self):
        MyClass.instance_count -= 1

