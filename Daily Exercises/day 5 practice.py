__author__ = 'stu'
import random

"""Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that 
are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don't worry if you can't figure this out at this point - we'll get to it soon)"""

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = []
length1 = random.randint(0,15) #generates length for list 1
length2 = random.randint(0,15) #generates length for list 2

def fillList(length,array): #fills an array
    array = [] #clears temparray
    for i in range(0,length+1): #creates length + 1 random integers to fill the list
        element = random.randint(0,100)
        array.append(element)
    return array

a = fillList(length1,common) #creates the first list
print a
b = fillList(length2,common) #creates the second list
print b
#testArray = b #arbitrarily sets testArray to b


"""if len(a) > len(b): #selects the longer array to go through, since it has more numbers to test
    testArray = a

for i in testArray: #tests inclusion of i in both arrays, by iterating through the testArray
    if i in a and i in b:
        common.append(i) #adds to common list
    elif i in common:
        None"""
for numA in a:
    if numA in common:
        None
    elif numA in b:
        common.append(numA)
    
print common