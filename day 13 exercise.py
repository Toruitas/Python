#exercise 13
#time taken

"""Write a program (function!) that takes a list and returns a new list that 
contains all the elements of the first list minus all the duplicates.

Extras:
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function."""
import random

testList = random.sample(range(10), random.randint(1, 10))
testList2 = [1, 2, 2, 2, 2, 2, 5, 2, 4, 3, 8, 9, 2, 9, 7]


def list_uniques_list(thislist):
    uniquelist = []
    for number in thislist:
        if number not in uniquelist:
            uniquelist.append(number)
    return sorted(uniquelist)


def list_uniques_set(thislist):
    sortedlist = set(thislist)
    sortedlist = list(sortedlist)
    return sortedlist
    
print(list_uniques_set(testList2))