__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/q8aom/2272012_challenge_16_easy/
Write a function that takes two strings and removes from the first string any character that appears in the second
string. For instance, if the first string is “Daily Programmer” and the second string is “aeiou ” the result is “DlyPrgrmmr”.
note: the second string has [space] so the space between "Daily Programmer" is removed
"""

def workhorse(string1, string2):
    temp = ""
    for ltr in string1:
        if ltr not in string2:
            temp+=ltr
        else:
            pass
    return temp

def smarter(string1, string2):
    for ltr in string2:
        string1 = string1.replace(ltr,"")
    return string1

if __name__ == "__main__":
    str1 = input("String 1")
    str2 = input("String 2")
    print(workhorse(str1,str2))
    print(smarter(str1,str2))