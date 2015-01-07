__author__ = "stu"

"""Let's say I give you a list saved in a variable: 
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes 
this list a and makes a new list that has only the even elements of this list in it.
"""

#first do a normal version

#numlist = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

import random
numlist = []
list_length =random.randint(5,15)

while len(numlist) < list_length:
    numlist.append(random.randint(0,99))

b = []
"""for num in a:
    if num %2 ==0:
        b.append(num)"""
        
#one liner

b = [num for num in numlist if num % 2 ==0]
print b