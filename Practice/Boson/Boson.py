__author__ = 'Stuart'

# Problem 1: convert C++ code to Python syntax

def problem_one(string1, string2):
    """
    Counts letters in each string, then compares the resulting dictionaries. This is done in O(n), linearly.
    :param string1:
    :param string2:
    :return:
    """
    if len(string1) != len(string1):
        return False

    letters_one = {}
    letters_two = {}
    
    for letter in string1:
        try:
            if letters_one[letter]:
                letters_one[letter] += 1
        except KeyError:
            letters_one[letter] = 1
    for letter in string2:
        try:
            if letters_two[letter]:
                letters_two[letter] += 1
        except KeyError:
            letters_two[letter] = 1

    if letters_two == letters_one:
        return True
    else:
        return False

def no_name(string1, string2):
    """
    Takes two strings. If they are NOT the same length, return False.
    If not, goes through strings, comparing first letter of str1 to all letters of str2.
    If there is a letter in str2 that matches the first letter of str1, calls no_name again, on processed strings.
    This should remove the matching letters from both strings.
    Once all matching letters are removed, we see if string2's length is 0.
    If it is not zero, we're basically saying that the two strings have the same amount of the same letters.
    :param string1:
    :param string2:
    :return: Boolean: if string2's length is 0.
    """
    if len(string1) != len(string2):
        return False

    for i in range(len(string2)):
        if string1[0] == string2[i]:
            return no_name(utility_function(string1,0),utility_function(string2,i))

    return len(string2)==0

def utility_function(str, j):
    """
    Had never looked at C++ before so, wasn't sure what "ret = new char[s.length -1]" was originally.
    Apparently it makes an array of length len(s)-1.

    Takes a string and an integer, removing letter from the string at that index.
    :param str: a string
    :param i: an integer
    :return: modified string, after removing letter at index j.
    """
    ret = ["?"]*(len(str)-1) # initializing the empty string as a list to use the C++ logic, and make replacing easier
    d = 0
    for k in range(len(str)):  # goes through indexes of the string
        if k == j:  # until the index matches the one passed from no_name... set d to 1.
            d = 1  # basically using this as a shift
        else:
            ret[k-d] = str[k] # replaces the char at ret[k-d(1)] with the char at str[k], shifting the string down

    return ''.join(ret)

####### My more pythonic versions -- didn't feel any need to modify the first one

def utility_function_2(str,j):
    """
    However if I was going to achieve this end goal in a Pythonic way, here's what I would do.
    No need for all the index shifting complexity, just return a sliced and reconstituted string.
    :param str: string
    :param j: index of char we want to remove
    :return: string minus the letter we don't want
    """
    return str[:j]+str[j+1:]