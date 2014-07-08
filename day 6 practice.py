__author__ = "stuart"

"""Ask the user for a string and print out whether this string is a palindrome 
or not. (A palindrome is a string that reads the same forwards and backwards.)"""

def palindrome(word):
    if len(word)==1 or len(word)==0:
        return True
    elif word[0]==word[-1]:
        return palindrome(word[1:-1])
    else:
        return False
        
def palindromeIterative(word):
    rev = word[::-1]
    if word == rev:
        return True
    else:
        return False
        
print palindrome('apple')
print palindrome('apapa')