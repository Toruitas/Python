__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/pxs2x/2202012_challenge_12_easy/
Write a small program that can take a string:
"hi!"
and print all the possible permutations of the string:
"hi!"
"ih!"
"!hi"
"h!i"
"i!h"
etc...
thanks to hewts for this challenge!
https://docs.python.org/3/library/itertools.html#itertools.permutations
"""

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:  # length of desired output longer than input, fails
        return
    indices = list(range(n))  # list of indicies for length n ('abcd': [0,1,2,3])
    cycles = list(range(n, n-r, -1))  # 'ABCD',2 would result in cycles of (4,2,-1) [4,3]
    yield tuple(pool[i] for i in indices[:r])  # first, print out tuple of unmodified input
    while n:  # as long as n exists
        for i in reversed(range(r)):  # [1,0] (runs twice in this case, since r=2)
            cycles[i] -= 1  # [4,2]; [3,2]|[3,1];[2,1]|
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]  # j=2; j=3|j=1;j=2|
                indices[i], indices[-j] = indices[-j], indices[i]
                # swap [0,1,2,3]->[0,2,1,3]->[2,0,1,3]|->[3,0,1,2]->[3,1,0,2]
                yield tuple(pool[i] for i in indices[:r])  # [acbd]
                break
        else:
            return


def permute(word, permuted=""):
    if word == "":
        print(permuted)
    else:
        for char in range(len(word)):
            permute(word[:char]+word[char+1:], permuted+word[char])

if __name__ == "__main__":
    import itertools
    string = input("Permutations for...?")
    print(["".join(char) for char in itertools.permutations(string)])  # prints list of joined permutations resulting from itertools' returned content