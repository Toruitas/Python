__author__ = 'Stuart'

"""
http://www.reddit.com/r/dailyprogrammer/comments/s6bas/4122012_challenge_39_easy/

You are to write a function that displays the numbers from 1 to an input parameter n, one per line, except that if the
current number is divisible by 3 the function should write “Fizz” instead of the number, if the current number is
divisible by 5 the function should write “Buzz” instead of the number, and if the current number is divisible by both 3
and 5 the function should write “FizzBuzz” instead of the number.

For instance, if n is 20, the program should write 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14,
FizzBuzz, 16, 17, Fizz, 19, and Buzz on twenty successive lines.
"""

def fizzbuzz(n):
    for num in range(1,n):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

def clever_fizzbuzz(num):
    for n in range(1,num+1):
        print((((n,"Buzz")[n%5==0],"Fizz")[n%3==0],"FizzBuzz")[n%15==0])
        # using 0 and 1 as T/F logic gates AND as tuple indexes. Super clever. Can we do better?