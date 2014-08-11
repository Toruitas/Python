__author__ = 'stuart leitch'

"""Create a program that asks the user for a number and then prints out a list 
of all the divisors of that number. (If you don't know what a divisor is, it is
a number that divides evenly into another number. For example, 13 is a divisor of 
26 because 26 / 13 has no remainder.)"""

number = int(raw_input("What number would you like to find divisors for?" )) #gets number to test
listRange = range(1,number+1) # sets range of values to compare
divisors = [] #empty list to add divisors to

for i in listRange: #iterates through the list of values
    if number % i == 0: #tests if it is a divisor
        divisors.append(i) #adds to list of divisors

print(divisors)