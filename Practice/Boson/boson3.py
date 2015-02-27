__author__ = 'Stuart'

"""
Given two vessels, one of which can accommodate 'a' liters of water and the other which can accommodate 'b' liters
of water, determine the number of steps required to obtain exactly c liters of water in one of the vessels.

At the beginning both vessels are empty. The following operations are counted as 'steps':
emptying a vessel,
filling a vessel,
pouring water from one vessel to the other,without spilling, until one of the vessels is either full or empty.

Input
An integer t, 1<=t<=100, denoting the number of test cases, followed by t sets of input data, each consisting of three
positive integers a (the number of liters the first container can hold), b (the number of liters the second container
can hold), and c (the final amount of liters of water one vessel should contain), not larger than 40000, given in
separate lines.

Output
For each set of input data, output the minimum number of steps required to obtain c liters, or -1 if this is impossible.

Sample Input:
2, 5, 2, 3, 2, 3, 4
Sample output:
2, -1
"""
import random

class bottle(object):
    def __init__(self,x):
        self.capacity = x
        self.current = 0

    def fill(self):
        self.current = self.capacity

    def pour(self, target_bottle):
        if target_bottle.capacity >= target_bottle.current + self.current:
            target_bottle.current += self.current
            self.current = 0
        else:
            self.current = (target_bottle.current + self.current - target_bottle.capacity)
            target_bottle.current = target_bottle.capacity

    def empty(self):
        self.current = 0

def fill_up(a, b, c):
    """
    Tries to fill up bottle c with bottles a and b.
    :param a: volume of bottle a
    :param b: volume of bottle b
    :param c: final volume either bottle should hold
    :param t: test cases
    :return: steps it takes to fill bottle, or -1 if impossible.
    """
    steps = 0
    emptyct = 0  # count for how many times we have emptied the large bottle. Stops endless loops.
    if c > a and c > b:  # if c is bigger than either bottle, not possible
        return -1
    if a == c or b == c:
        return 1 # one step to fill
    elif max(a, b)-min(a, b) == c:
        return 2 # one to fill big, one to pour into small. Remainder will be c.
    elif a > b:  # instantiates objects
        big_bottle = bottle(a)
        small_bottle = bottle(b)
    else:
        big_bottle = bottle(b)
        small_bottle = bottle(a)

    while small_bottle.current != c and big_bottle.current != c:
        #print(small_bottle.current,big_bottle.current, emptyct)
        steps += 1
        if emptyct >2:  # doing two empty cycles seems to go through all relevant nums, preventing endless loop
            return -1
        if big_bottle.current == big_bottle.capacity:
            big_bottle.empty()
            emptyct += 1
        elif big_bottle.current - (small_bottle.capacity-small_bottle.current) == c:  # edge case where one move of the big bottle into small
            big_bottle.pour(small_bottle)  # will fill small, leaving the remainder as c
        elif big_bottle.current < big_bottle.capacity and small_bottle.current != 0:
            small_bottle.pour(big_bottle)
        else:# small_bottle.current == 0:
            small_bottle.fill()

    return steps

def run_test():
    """
    sets is a list of sets

    Not sure how you wanted to input test sets, so I just did it with user input. No error/type checking.

    :param test_cases: number of tests to run
    :param sets: list of sets of data [[7,3,1],[7,6,1],...]
    :return:
    """
    t = int(input("How many tests and sets to run?"))
    sets = []
    for test in range(t):  # set test parameters
        a = int(input(("Volume of 1st bottle?")))
        b = int(input("Volume of 2nd?"))
        c = int(input("Goal volume?"))
        sets.append([a,b,c])

    for s in sets:
        print(fill_up(s[0],s[1],s[2]))

run_test()