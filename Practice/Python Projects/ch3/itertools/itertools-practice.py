__author__ = 'Stuart'

import itertools as it
import operator

# DEMONSTRATE COUNT
# for n in it.count(15,2):
#     if n < 40:
#         print(n, end=" ")  # is this any different than print(n, " ")?
#         #print(n, " ")  # yes it is, because otherwise the end defaults to \n (newline)
#     else:
#         break

# DEMONSTRATE REPEAT
# for n in range(7):
#     print(next(it.repeat('yes ')), end="")
#
# print(list(it.repeat(6,3)))

# DEMONSTRATE CYCLE
# res1 = []
# res2 = []
# res3 = []
# resources = it.cycle([res1,res2,res3])
# for n in range(30):  # iterates through 0-30...
#     res = next(resources)  # on each round, we reassign res to the next in resources
#     res.append(n)  # then we call the append method on the res# that we cycled to, and append n.
# print(res1, res2, res3)

# DEMONSTRATE CHAIN
# items = it.chain([1,2,3],'astring',{'a','set','of','strings'})  # mixed types. List, string, set.
# for item in items:  # iterates over whatever is iterable in the items
#     print(item)

# DEMONSTRATE ISLICE
# data = list(range(20))
# print(data[3:12:2])
# for d in it.islice(data,3,12,2):
#     print(d,end=' ')

# DEMONSTRATE COMPRESS
# for item in it.compress([1,2,3,4,5],[False, True, False, 0, 1]):
#     print(item)

#FILTER FALSE
# for item in it.filterfalse(lambda e: e % 2 == 0, [1,2,3,4,5]):
#     print(item)

#DROPWHILE
# def singleDigit(n):  # True if a single digit number
#     return n < 10
# for n in it.dropwhile(singleDigit, range(20)):  # will print if > 10
#     print(n, end=' ')
# print()
# for n in it.takewhile(singleDigit,range(20)):  # will print if < 10
#     print(n, end=' ')
# print()
# for n in it.dropwhile(singleDigit,[1,2,12,4,20,7,999]):
# # they both stop processing data (using singleDigit) after the first trigger
#     print(n, end=' ')

#ACCUMULATE
# https://docs.python.org/3/library/itertools.html#itertools.accumulate
# for n in it.accumulate([1,2,3,4]):  # defaults to add
#     print(n, end=' ')
# for n in it.accumulate([1,2,3,4,5], operator.mul):  # multiplies
#     print(n, end=' ')

data = [[1,2,3,4,5],[6,7,8,9,0],[0,2,4,6,8],[1,3,5,7,9]]
# for d in data:
#     print(all(d))  # returns True when all input data items are True
    # middle two lists are False because they have 0 in them
# for key, group in it.groupby(data, key=all):
#     print(key,group)
    # doing this alone creates two groups keyed on True
    # True <itertools._grouper object at 0x000000000054D4E0>
    # False <itertools._grouper object at 0x000000000054D7F0>
    # True <itertools._grouper object at 0x000000000054D518>
    # so we have to process first
# for key, group in it.groupby(sorted(data,key=all),key=all):  # sort it by T/F
#     print(key, group)
# for key, group in it.groupby(sorted(data,key=all),key=all):
#     if key:
#         trueset = group
#     else:
#         falseset = group
#
# for item in falseset:  # this is empty... why?
#     print(item)  # because falseset group was created first and then the iterator moved on, invalidating that value

groups = {True:[], False:[]}  # first gotta do this
for key, group in it.groupby(sorted(data,key=all),key=all):
    groups[key].append(list(group))  # then append to appropriate key. Keys have to match up of course.
print(groups)
