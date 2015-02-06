__author__ = 'Stuart'

from lendydata import *
from itertools import *

# def cost(item):   This actually already exists in lendydata.py, which we imported
#     return int(item[4][1:])

for n in islice(accumulate(cost(item) for item in items[1:]), len(items[1:])-1, None):
    # first accumulates a list for the costs of each items.
    # Then slice from index -1 to end to get the final total.
    # islice args have to be positive ints, so have to find len(items)-2 to get index[-1] because of headers
    # or, as I modified it, len(items[1:])-1 to account for headers.
    # none doesn't have to be here... This seems like an inefficient way of going about this function tbh.
    # it's only one number at the end...
    print(n)

print(n/(len(items[1:])))  # to get the average, we still have n in scope. So we can use that.

# def owner(item):    # also in lendydata.py already
#     return item[3]

owners = {}
for key, group in groupby(sorted(items[1:], key = owner), key = owner):
    # first sort the items (except for header) by owner method, which gets ownerID.
    # then group by owner IDs, and save how many they own into dictionary based on owner ID.
    owners[key] = len(list(group))  # length of the person's group is how many items they own

for member in members[1:]:  # for each member beyond the header...
    print(member[1],' : ', owners[member[0]])  # print their name and how many things they own (the value of their key)

def returned(loan):  # if a loan hasn't been returned, return False
    return not (loan[-1] == 'None')

print([items[int(loan[1])]for loan in filterfalse(returned,loans)])
# filter through the loans for the False one, as it isn't returned yet.