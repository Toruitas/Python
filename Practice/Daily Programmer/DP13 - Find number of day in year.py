__author__ = 'Stuart'
"""
http://www.reddit.com/r/dailyprogrammer/comments/pzo4w/2212012_challenge_13_easy/
Find the number of the year for the given date. For example, january 1st would be 1, and december 31st is 365.
for extra credit, allow it to calculate leap years, as well.
https://docs.python.org/3.4/library/datetime.html
http://www.tutorialspoint.com/python/python_date_time.htm
"""

def test_leap(date):
    """
    Year evenly divisible by 4, by 400, but not 100.
    :param date:
    :return:Boolean for leap year confirmation
    """
    if date % 400 != 0 and date % 100 == 0:
        return False
    elif date %4 == 0:
        return True
    else:
        return False

def lazyway(year,month,day):
    """
    Returns number of day in teh year. Includes leap year calculation already. Super Lazy.
    d.timetuple() == time.struct_time((d.year, d.month, d.day, 0, 0, 0, d.weekday(), yday, -1))
    yday = d.toordinal() - date(d.year, 1, 1).toordinal() + 1 is the day number within the current year starting with 1 for January 1st.
    :param year: Year you wanna check
    :param month: Month
    :param day: Day
    :return: ordinal date in the year
    """
    that_day = datetime.date(year,month,day)
    return that_day.timetuple()[7]

if __name__ == "__main__":
    import calendar # if I were a lazy man, I could use this to test for leapness
    import datetime # or could use date.timetuple()'s yday to find it easily from a date object
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
    days = [31,28,31,30,31,30,31,31,30,31,30,31] #days in each month
    thedate = input("What is the date you want to test? Format January 21st, 1987 please.")
    thedate = thedate.split()
    thedate[0],thedate[1],thedate[2] = thedate[0].lower(),int(thedate[1].replace("st","").replace("th","").replace(",","")),int(thedate[2])
    month_index = months[thedate[0]]-1 #since month indexes start at 1 in the dictionary, but 0 in the days list
    year = thedate[2]
    month = months[thedate[0]] #months start at 1 for this library too, so no need to -1
    day = thedate[1]
    print(lazyway(year,month,day))
    if test_leap(thedate[2]): #test for leapness
        days[1] += 1
    numday = 0
    for i in range(month_index): #adds all the months before the entered month
        numday += days[i]
    numday += thedate[1] #then adds the date of current month
    print(numday)