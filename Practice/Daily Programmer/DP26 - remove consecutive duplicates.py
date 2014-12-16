__author__ = 'Stuart'
"""
you have a string "ddaaiillyypprrooggrraammeerr". We want to remove all the consecutive duplicates and put them in a separate string, which yields two separate instances of the string "dailyprogramer".
use this list for testing:
input: "balloons"
expected output: "balons" "lo"
input: "ddaaiillyypprrooggrraammeerr"
expected output: "dailyprogramer" "dailyprogramer"
input: "aabbccddeded"
expected output: "abcdeded" "abcd"
input: "flabby aapples"
expected output: "flaby aples" "bap"
http://www.reddit.com/r/dailyprogrammer/comments/qzil1/3162012_challenge_26_easy/
"""

def strip_dups(string):
    """
    takes string, strips consecutive duplicates, returns string of duplicates and one without
    :param string:
    :return:
    """
    dups = []
    for char in string:
        try:
            if char == string[string.index(char)+1]:
                dups.append(string[string.index(char)+1])
                string = string[:string.index(char)] + string[string.index(char)+1:]
            else:
                pass
        except IndexError:
            pass
    return string, dups

def strip_dups_2(string):
    stripped1 = ''
    stripped2 = ''
    for c in string:
        try:
            if string[string.index(c)+1] == c:
                stripped1 += c
            else:
                stripped2 += c
        except IndexError:
            pass
    return stripped1,stripped2

def dup_strings(x):
    from itertools import groupby, islice
    return (''.join(key for key, group in groupby(x)),
            ''.join(''.join(islice(group, 1)) for key, group in groupby(x)))

def stripDuplicates(given):
    strip = []
    dup = []
    for cnt in range(len(given)):
        if given[cnt-1] == given[cnt]:
            dup.append(given[cnt])
        else:
            strip.append(given[cnt])
    #print(''.join(strip))
    #print(''.join(dup))
    return [strip, dup]

def remove_duplicate_chars(initialString):
    import re
    truncatedString = ''
    removedDuplicates = ''

    for match in re.finditer(r'([\s\w])(\1+)?', initialString, flags=0): #(group1)(group2 repeat of group 1 optional?)
    # \1 means first group
    # https://docs.python.org/3.4/library/re.html#re.match.group
    # https://docs.python.org/3.4/library/re.html#re.finditer : returns matches for (pattern, string)
        truncatedString += match.group(1) #the first paranthesized subgroup  - bb's first b
        removedDuplicates += match.group(0)[:-1] #the whole match, but everything up to the last letter

    return [truncatedString, removedDuplicates]

if __name__ == "__main__":
    string = ["balloons","ddaaiillyypprrooggrraammeerr","aabbccddeded","flabby aapples"]
    #print(map(strip_dups(string),string))
    for s in string:
        #print(stripDuplicates(s))
        print(remove_duplicate_chars(s))