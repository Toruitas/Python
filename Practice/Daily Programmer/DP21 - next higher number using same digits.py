__author__ = 'Stuart'
"""
Input: a number
Output : the next higher number that uses the same set of digits.
http://www.reddit.com/r/dailyprogrammer/comments/qp3ub/392012_challenge_21_easy/
"""
def permutate_alt(n):
    from itertools import permutations
    normal = []
    for permutation in permutations(n):
        perm = ''.join(permutation)
        normal.append(int(perm))
    normal.sort()
    index = normal.index(int(n))
    return normal[index+1]


if __name__ == "__main__":
    import itertools
    number = "1342"#(input("What is your number?"))
    options = itertools.permutations(number)
    listed = [''.join(char) for char in options]
    listed.sort()
    index = listed.index(number)
    print(listed[index+1])
    print(permutate_alt(argv[1]))