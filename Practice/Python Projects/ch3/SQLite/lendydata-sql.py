__author__ = 'Stuart'

import sqlite3

members = [
    ['Fred','fred@lendylib.org'],
    ['Mike','mike@gmail.com'],
    ['Joe','joe@joesmail.com'],
    ['Rob','rjb@somcorp.com'],
    ['Anne','annie@bigbiz.com']
]

member_sql = '''insert into member (Name, Email) values (?, ?)'''

items = [
    ['Lawnmower','Tool',     0, 150,'Excellent', '2012-01-05'],  # SQLite needs dates formatted this way
    ['Lawnmower','Tool',     0, 370,'Fair',      '2012-04-01'],  # since it has functions that can create normal
    ['Bike',     'Vehicle',  0, 200,'Good',      '2013-03-22'],  # date strings. Improves data quality.
    ['Drill',    'Tool',     0, 100,'Good',      '2013-10-28'],  # SQLite also has a version of strftime()
    ['Scarifier','Tool',     0, 200,'Average',   '2013-09-14'],  # Always uses UTC/GMT. So need to use time funcs
    ['Sprinkler','Tool',     0, 80, 'Good',      '2014-01-06']   # inside python to change them
]  # owner field is Not Null, so fill with dummy 0 that is overwritten later

item_sql = '''
insert into item
(Name, Description, ownerID, Price, Condition, DateRegistered)
values (?, ?, ?, ?, ?, date(?))'''

set_owner_sql = '''
UPDATE item
SET OwnerID = (SELECT ID FROM member WHERE name = ?)
WHERE item.id = ?
'''

loans = [
    [1,3,'2012-01-04','2012-04-26'],
    [2,5,'2012-09-05','2013-01-05'],
    [3,4,'2013-07-03','2013-07-22'],
    [4,1,'2013-11-19','2013-11-29'],
    [5,2,'2013-12-05',None]
]

loan_sql = '''
insert into loan
(itemID, BorrowerID, DateBorrowed, DateReturned)
values (?, ?, date(?),date(?))'''  # variable values are inserted where the ? are. like using {}
# {} isn't used here since it is vulnurable to an injection attack

db = sqlite3.connect('lendy.db')
cur = db.cursor()


"""
these three below make inserts into lendy.db
since we already ran this once, no need to do again
"""
cur.executemany(member_sql,members)  # takes statement and sequence/iterator/generator
cur.executemany(item_sql,items)  # and repeatedly applies statement
cur.executemany(loan_sql,loans)  # alternatively could use a for loop and normal execute

owners = ('Fred','Mike','Joe','Rob','Anne','Fred')
for item in cur.execute("select id from item").fetchall():  # goes through owners and reassigns their ownership
    itemID = item[0]
    cur.execute(set_owner_sql,(owners[itemID-1],itemID))
    # owners list isn't the members table from above, but the list just two lines up...

cur.close()
db.commit()
db.close()