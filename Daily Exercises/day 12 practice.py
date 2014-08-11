#exercise 12
#time taken 5 minutes

"""Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function."""

a = [5, 10, 15, 20, 25, 90]

def first_and_last(list):
    return [list[0],list[-1]]

print first_and_last(a)