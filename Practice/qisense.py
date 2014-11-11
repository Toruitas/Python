__author__ = 'Stuart'
"""
Q1.
Given a array of 10,000 random intergers, select the biggest 100 numbers.

1) The order of the result numbers does not matter;
2) Take care about the algorithm performance and big O complexity.

Q2.
Find the string which has this hash: 25267566250558
The string has length 8.
Characters can be from: c,e,i,a,r,w,u,s,p

The hash function works like this:
hash(str):
    1. LETTERS = c, e, i, a, r, w, u, s, p
    2. h = 7
    3. for c in str:
        1. i = index of c in LETTERS
        2. h = 37 * h + i
    4. return h

Please send us the string you found, and the code you used to find it.
"""

def q1():
    """
    Create list, fill it until len = 100, then if each compared number higher than minimum in the list, replace.
    Skips repeat integers if they are already in the top_list, but likely original list has no repeats, since
    random integers are generated up to 1 million.
    :param list: list of integers. Or use the generator. With a list of only 10,000 performance isn't so much of an issue.
    :return:list of top 100 unique integers
    """
    import random
    top_list = []
    length_top_list = 100  # for ease of testing
    gen = (random.randrange(1000000) for i in range(10000))  # generates 10,000 random numbers from [0:1,000,000)

    for integer in gen:
        if len(top_list) < length_top_list:  # if list isn't full, fill it up
            top_list.append(integer)
        elif integer in top_list:  # This elif clause filters out non-unique integers by doing nothing.
            pass  # If repeats allowed, just ignore
        elif integer > min(top_list):  # if the number is higher than the smallest number in the top_list, replaces
            top_list[top_list.index(min(top_list))] = integer
        else:  # shouldn't be reached
            print("'surprise!' is the answer to q2")
    return top_list


def hasher(str):
    LETTERS = "ceiarwusp"
    h = 7
    for c in str:
        i = LETTERS.index(c)
        h = 37 * h + i
    return h

def find_string_recursive(hash = 25267566250558):
    """
    decrypts a given hashcode according to given hash function
    hash = 25267566250558
    string has length 8
    76484271
    surprise
    :param hash: hash code for a string
    :return: decrypted string
    """
    #simple modulus will give you the index of the last letter:1 .'. "e" is last digit
    LETTERS = "ceiarwusp"
    indy = int(hash%37)  # indy is index of letters.
    if ((hash-indy)/37) == 7:
        return LETTERS[indy]
    else:
        return find_string_recursive((hash-indy)/37) + LETTERS[indy]

print(find_string_recursive())
print(q1())
