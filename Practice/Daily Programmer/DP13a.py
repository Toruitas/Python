__author__ = 'Stuart'
import sys

class DaysException(Exception):
    def __init__(self, day, month):
        self.day = day
        self.month = month
    def __str__(self):
        months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
            'October', 'November', 'December')
        return "{0} is more than the number of days in a {1}".format(self.day, months[self.month-1])

class MonthException(Exception):
    def __init__(self, month):
        self.month = month
    def __str__(self):
        return "{0} does not correspond with a valid month".format(self.month)

def days(day, month):
    months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30)
    if month > 12 : raise MonthException(month)
    if day > months[month-1] : raise DaysException(day, month)
    return sum(months[:month-1]) + day

try :
    print( days( int(sys.argv[1]), int(sys.argv[2]) ) )
except Exception as e:
    print(e)