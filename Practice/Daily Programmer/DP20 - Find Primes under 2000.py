__author__ = 'Stuart'
"""
create a program that will find all prime numbers below 2000
http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
http://en.wikipedia.org/wiki/Fermat%27s_little_theorem
http://www.reddit.com/r/dailyprogrammer/comments/qnkro/382012_challenge_20_easy/
"""
import math

maxnum = 2000
L2 = list(range(2,maxnum))

for i in range(2,int(math.sqrt(maxnum))):
    if i in L2:
        for j in range(i**2,2000,i):
            try:
                L2.remove(j)
            except:
                pass
print(L2)