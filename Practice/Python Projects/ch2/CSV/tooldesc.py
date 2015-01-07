__author__ = 'Stuart'

import csv, datetime

items = [
    ['1','Lawnmower','Small Hover mower','Fred','$150','Excellent','2012-01-05'],
    ['2','Lawnmower',"Ride-on mower","Mike","$370","Fair","2012-04-01"],
    ["3","Bike","BMX bike","Joe","$200","Good","2013-03-22"],
    ["4","Drill","Heavy duty hammer","Rob","$100","Good","2013-10-28"],
    ["5","Scarifier","Quality, stainless steel","Anne","$200","2013-09-14"],
    ["6","Sprinkler","Cheap but effective","Fred","$80","2014-01-06"]
]

def write_tooldesc():
    """
    writes the above list to a csv file.
    With commented out modifying of date formatting for last date.
    :return:
    """
    with open('tooldesc.csv','w', newline='') as tooldata:
        toolwriter = csv.writer(tooldata)
        for item in items:
            # temp = datetime.datetime.strptime(item[-1],"%Y-%m-%d")  # creates a datetime object
            # item[-1] = temp.strftime("%b %d, %Y")
            # print(item)
            toolwriter.writerow(item)


def read_toolhire():
    """
    opens toolhire, and prints it to console in dict format.
    Header from csv file columns is dictionary key. Returns series of dictionaries line by line
    Dictionaries are of course not in the original order.
    :return:
    """
    with open('toolhire.csv') as th:
        rdr = csv.DictReader(th)
        for item in rdr:
            print(item)


def analysis():
    """
    to find what Fred owns, we can do this.
    Builds a list of items fred owns.
    Can also do with a list version if we use list indicies
    e.g...
    :return:
    """
    with open('toolhire.csv') as th:
        rdr = csv.DictReader(th)
        items = [item for item in rdr]

    fred = [item['Name'] for item in items if item['Owner']=='Fred']
    print(fred)
    # [item[1] for item in toolList if item[3] == 'Fred']