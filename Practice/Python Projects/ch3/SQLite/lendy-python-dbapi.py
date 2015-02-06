__author__ = 'Stuart'

import sqlite3
db = sqlite3.connect(':memory:')  # creates temporary DB in RAM
cur = db.cursor()  # creates cursor obj
cur.execute("create table test(id,name)")  # create test table
cur.execute("INSERT INTO test (id,name) VALUES (1,'Alan')")  # record1
cur.execute("INSERT INTO test (id,name) VALUES (2,'Laura')")
cur.execute("INSERT INTO test (id,name) VALUES (3, 'Jennifer')")
cur.execute("SELECT * FROM test")  # select all data from table into the cursor
# print(cur.fetchall())  #  fetchall views output as a list of tuples.

def findData(cursor, aString):
    """
    finds records that match the string and returns them
    :param cursor:
    :param aString:
    :return:
    """
    cursor.execute("SELECT * FROM test WHERE name LIKE ?",(aString,))
    return cur.fetchall()

print(findData(cur,'A%'))  # finds record with big A at start
print(findData(cur,'%a%'))  # finds all records with a in the middle

cur.execute("DELETE FROM test")  # deletes all records in tables
cur.execute("DROP TABLE test")  # deletes tables
cur.close()  # close the cursor
db.commit()  # always commit before closing
db.close()

