__author__ = 'Stuart'
"""
Often times in commercials, phone numbers contain letters so that they're easy to remember (e.g. 1-800-VERIZON).
Write a program that will convert a phone number that contains letters into a phone number with only numbers and the
appropriate dash. Click here[1] to learn more about the telephone keypad.
Example Execution: Input: 1-800-COMCAST Output: 1-800-266-2278

https://docs.python.org/3/library/stdtypes.html#str.maketrans
"""

def alternative():
    import string, sys
    table = str.maketrans(string.ascii_letters, '22233344455566677778889999' * 2)
    basic = sys.argv[1].translate(table, '-')
    print('{0}-{1}-{2}-{3}'.format(basic[0], basic[1:4], basic[4:7], basic[7:]))

if __name__ == "__main__":
    import string
    transtable = str.maketrans(string.ascii_letters, '22233344455566677778889999'*2)
    translated = ((input("Input a phone number")).translate(transtable))
    translated = translated[:-4]+"-"+translated[-4:]
    print(translated)