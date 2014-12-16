__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/rmmn8/3312012_challenge_34_easy/
A very basic challenge:
In this challenge, the
input is are : 3 numbers as arguments
output: the sum of the squares of the two larger numbers.
Your task is to write the indicated challenge.
"""

def do_work(num1,num2,num3):
    ordered = sorted([num1,num2,num3])
    return ordered[1]**2 + ordered[2]**2

def square_sum(a, b, c):
    nums = [a, b, c]
    one = max(nums)
    nums.remove(one)
    return one**2 + max(nums)**2

if __name__ == "__main__":
    print(do_work(1,3,2))