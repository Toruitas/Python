__author__ = 'Stuart'
"""
The array duplicates problem is when one integer is in an array for more than once.
If you are given an array with integers between 1 and 1,000,000 or in some other interval and one integer is in the array twice. How can you determine which one?
Your task is to write code to solve the challenge.
Note: try to find the most efficient way to solve this challenge.
http://www.reddit.com/r/dailyprogrammer/comments/r59kk/3202012_challenge_28_easy/
"""

def bad(array):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                print("Duplicate found, array[%d] and array[%d] are both equal to %d" % (i, j, array[i]))

def better(array):
    array2 = [(v, i) for i,v in enumerate(array)]
    array2.sort()

    for i in range(len(array2)-1):
        if array2[i][0] == array2[i+1][0]:
            print("Duplicate found, array[%d] and array[%d] are both equal to %d" % (array2[i][1], array2[i+1][1], array2[i][0]))

def best(array):
    hashtable = {}

    for i,v in enumerate(array): #enumerate returns a tuple of (count = 0 ++, value)
        if v in hashtable:
            print("Duplicate found, array{0} and array{1} are both equal to {2}".format(hashtable[v], i, array[i]))

        hashtable[v] = i #hashes using the value as key, count as value

    print("")