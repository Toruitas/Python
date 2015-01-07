__author__ = 'Stuart'

"""
1. How convert between data types?
A: Like int() float() list() etc. Data quality issues arise between int-float conversion.
Custom types such as frozen sets can be used as well.
2. What can be the key in a dictionary? Anything immutable, such as an int, string, or tuple.
What can be a value? Anything, including another dictionary.
5. An infinite loop in a while loop can be caused if the conditional is never broken.
For example, if there was no incrementor, or way to Falsify a While True.
This could cause the computer to lock up and use tons of memory.
Make sure to always have a way to break the loop.
"""

def three(x):
    if x > 10:
        print('blue')
    elif x > 8:
        print("eight")
    elif x > 5:
        print("five")
    else:
        print("banana")

def three_point_five():
    (red, orange, yellow, green, blue, violet) = range(6)
    # it looks like this line sets 0 to red, 1 to orange... overriding the normal 0,1,2?

    color = int(input('Type a number between 1 and 6'))-1
    if color == red:
        print('You picked red.')
    elif color == orange:
        print('You picked orange')
    elif color == yellow:
        print('You picked yellow.')
    elif color == green:
        print('You picked green')
    else:
        print("I don't like your color choice.")

def four():
    for i in range(7):
        print("{} times".format(i+1))

def six(base,height):
    print(base*height /2)

class Seven(object):
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        if self.count > 9:
            self.count = 0
        return self.count

    def reset(self, value =0):
        current_val = self.count
        if 0 < value < 9:
            self.count = value
        else:
            raise ValueError("Value must be between 0 and 9")
        return current_val