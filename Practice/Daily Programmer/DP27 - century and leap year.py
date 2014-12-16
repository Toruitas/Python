__author__ = 'Stuart'
"""
Write a program that accepts a year as input and outputs the century the year belongs in (e.g. 18th century's year ranges are 1701 to 1800) and whether or not the year is a leap year. Pseudocode for leap year can be found here[1] .
Sample run:
Enter Year: 1996
Century: 20
Leap Year: Yes
Enter Year: 1900
Century: 19
Leap Year: No
http://www.reddit.com/r/dailyprogrammer/comments/r0r3h/3172012_challenge_27_easy/
"""

def century(year):
    import calendar
    results = {}
    if year[-2:] == "00":
        results["century"] = ("{0}th".format(year[-4:-2]))
        #return (year[-4:-2]), calendar.isleap(int(year))
    else:
        results["century"] = ("{0}th".format(int(year[-4:-2])+1))
        #return (int(year[-4:-2])+1 , calendar.isleap(int(year)))
    if calendar.isleap(int(year)):
        results["leap"] = "Yes"
    else:
        results["leap"] = "No"
    return results

def round_two():
    import sys
    from math import floor
    from calendar import isleap

    def century(year):
        if year % 100 is 0:
            return year / 100
        else:
            return int(floor( year/100) + 1)

    while True:
        try:
            year = int(input("Enter year: "))
            print("Century: {0}\nLeap year: {1}\n".format(
                century(year),
                isleap(year)))
        except KeyboardInterrupt:
            sys.exit()
        except ValueError:
            print("Not a valid year.  Try again\n")

print(century("1900"))