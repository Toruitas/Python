_author_ = 'stu'

#exercise 11
#time to complete: 15 minutes

"""Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.)
You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below."""

"""
def get_integer(help_text="Give me a number: "): #using help_text = gives it a default argument, for when there is no argument submitted
    return int(input(help_text))

age = get_integer("Tell me your age: ")
school_year = get_integer("What grade are you in? ")
if age > 15:
    print("You are over the age of 15")
print("You are in grade " + str(school_year))
"""

def get_number(help_text="Give me a number: "): #gets number to test from user
    return int(input(help_text))

def prime_test(number):
    divisors = []
    for i in range(2,number/2 +1): #iterates through the list of values. Excludes 1, by definition of prime only divisible by self and 1.
        if number % i == 0: #tests if it is a divisor
            divisors.append(i) #adds to list of divisors
    if len(divisors) == 0: #if any numbers tested have been added to the list, returns prime/not prime
        return number," is a prime number."
    else:
        return number," is not a prime number."
        
print prime_test(get_number("Give me a number to test: "))