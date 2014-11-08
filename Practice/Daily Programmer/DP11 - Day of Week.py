__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/pwons/2192012_challenge_11_easy/

The program should take three arguments. The first will be a day, the second will be month, and the third will be year.
Then, your program should compute the day of the week that date will fall on.
http://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week

http://labix.org/python-dateutil
http://pymotw.com/2/datetime/
https://docs.python.org/3.4/library/calendar.html#module-calendar
https://docs.python.org/3.4/library/datetime.html
http://pastebin.com/C6zSSiMZ

"""
def elegant():
    """
    https://docs.python.org/2/library/sys.html
    :return:
    """
    from sys import argv #argv so you enter arguments from command line when launching
    from calendar import weekday, day_name
    [day, month, year] = map(int, argv[1:]) #r = map(func, seq)
    print(day_name[weekday(year, month, day)])

def nearly_elegant():
    import sys
    import calendar

    months = {
    'january':1,
    'february':2,
    'march':3,
    'april':4,
    'may':5,
    'june':6,
    'july':7,
    'august':8,
    'september':9,
    'october':10,
    'november':11,
    'december':12
    }

    weekday = {
    0:'monday',
    1:'tuesday',
    2:'wednesday',
    3:'thursday',
    4:'friday',
    5:'saturday',
    6:'sunday',
    }

    def get_args():
        "Returns a dict of args"
        if len(sys.argv) <= 3:
            print("Not enough arguments!")
            print("I need:")
            print("\tThe day [1]")
            print("\tThe month [2]")
            print("\tThe year [3]")
            sys.exit(0)

        try:
            month = months[sys.argv[2].lower()]
        except:
            try:
                month = int(sys.argv[2])
            except:
                month = months[sys.argv[2]]

        return {'day': int(sys.argv[1]),'month':month,'year':int(sys.argv[3])}

    def main(year,month,day):
        int_day = calendar.weekday(year,month,day)
        print(weekday[int_day])

    if __name__ == "__main__":
        date = get_args()
        year = date['year']
        month = date['month']
        day = date['day']
        main(year,month,day)


if __name__ == "__main__":
    import datetime
    months = {"january":1,
              "february":2,
              "march":3,
              "april":4,
              "may":5,
              "june":6,
              "july":7,
              "august":8,
              "september":9,
              "october":10,
              "november":11,
              "december":12}
    dayweek = {0:"Monday",
               1:"Tuesday",
               2:"Wednesday",
               3:"Thursday",
               4:"Friday",
               5:"Saturday",
               6:"Sunday"}
    thedate = input("You want ot find the day of the week for which date? In format December 21, 1987, please")
    thedate = thedate.replace(",","").split()
    if len(thedate[1])>2: #if user enters 21st rather than 21, removes it. 3rd 5th
        thedate[1] = thedate[1][:2]
    try:
        thedate[1] = int(thedate[1])
        thedate[2] = int(thedate[2])
        thedate[0] = months[thedate[0].lower()]
        print(thedate)
    except TypeError or KeyError:
        print("Not a valid date")
    weekday = (datetime.date(thedate[2],thedate[0],thedate[1]).weekday())
    print(dayweek[weekday])