__author__ = 'Stuart'
"""
A Palindrome[1] is a sequence that is the same in reverse as it is forward.
I.e. hannah, 12321.
Your task is to write a function to determine whether a given string is palindromic or not.
Bonus: Support multiple lines in your function to validate Demetri Martin's 224 word palindrome poem[2] .
Thanks to _lerp for submitting this idea in /r/dailyprogrammer_ideas[3] !
http://www.reddit.com/r/dailyprogrammer/comments/r8a70/3222012_challenge_29_easy/
http://www.pastemagazine.com/articles/2009/02/demetri-martins-palindrome-poem.html
"""



"""
find a way to directly import the text from the website, maybe use BS4?
strip spaces and punctuation
slice slice baby
"""

def palindrome_test(str):
    """
    strips strings of punctuation and whitespace and also lowercases it for proper comparisons
    :param str:
    :return:
    """
    import string
    simple_string = ''.join(letter.lower() for letter in str if letter not in string.punctuation and letter not in string.whitespace)
    while len(simple_string)>1:
        if simple_string[0] != simple_string[-1]:
            return False
        else:
            simple_string = simple_string[1:-1]
    return True

def load_simplify(source):
    """
    goes through series of lines. If all are individual palindromes, returns true. Else, false.
    :param source:
    :return:
    """
    with open(source,"r") as original:
        for line in original:
            if not palindrome_test(line):
                return False
            else:
                pass
        return True
    #shutil.move("temp.txt",source)

def one_string(source):
    """
    Turns a multi line thing like the poem, where the palindrome spans multiple lines, into one line for processing
    :param source: Source file - doesn't process multiline string otherwise
    :return: single line palindrome from multi line one
    """
    str = ''
    with open(source,"r") as original:
        for line in original:
            str+=line
    return str

def RE_vers(string):
    import re

    palindrome = lambda s: s == s[::-1]

    def is_palindrome(s):
        """Determines if the given string is a palindrome. Supports multiple lines."""
        return palindrome(re.sub('\W', '', str(s).lower()))

def lazy(s):
    s = s.lower() #Not sure if required, is "Hannah" still a palindrome? My guess was yes
    return s == s[::-1]


if __name__ == "__main__":
    source = "DP29 - Palindrome.txt"
    if source[-4] == ".":
        if (load_simplify(source)):
            print(load_simplify(source))
        else:
            print(palindrome_test(one_string(source)))
    else:
        print(palindrome_test(source))