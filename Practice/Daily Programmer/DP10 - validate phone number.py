__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/pv98f/2182012_challenge_10_easy/

The exercise today asks you to validate a telephone number, as if written on an input form. Telephone numbers can be written as ten digits, or with dashes, spaces, or dots between the three segments, or with the area code parenthesized; both the area code and any white space between segments are optional.
Thus, all of the following are valid telephone numbers: 1234567890, 123-456-7890, 123.456.7890, (123)456-7890, (123) 456-7890 (note the white space following the area code), and 456-7890.
The following are not valid telephone numbers: 123-45-6789, 123:4567890, and 123/456-7890.
source: programmingpraxis.com
"""

if __name__ == "__main__":
    import re
    pattern1 = r'\D*\d{0,3}?\D*\d{3}\D*\d{4}'
    pattern2 = re.compile(r'''
        [\d]{10} #full 10 digit number together: 1234567890
        | #or
        ([\d]{3}-)? # optional prefix ending in a dash
        [\d]{3}-[\d]{4} #mandatory 7 digits separated by a dash
        | #or
        [\d]{3}\.[\d]{3}\.[\d]{4} #like above but separated by .
        | #or
        \([\d]{3}\)[ ]?[\d]{3}-[\d]{4} # like above but separated by () and with an optional [space] after parentheses
        ''',re.VERBOSE) #Verbose version to keep things more readable
    bracketed = re.compile(r'\([\d]{3}\) ?[\d]{3}[-| |.]?[\d]{4}')
    non_bracketed = re.compile(r'^[\d]{3}?[-| |.]?[\d]{3}[-| |.]?[\d]{4}')
    numbers = ["1234567890","123-456-7890","123.456.7890","(123)456-7890","(123) 456-7890","456-7890","123-45-6789","123:4567890","123/456-7890"]
    for item in numbers:
        if item[0] == "(":
            print(re.fullmatch(bracketed,item))
        else:
            print(re.fullmatch(non_bracketed,item))
