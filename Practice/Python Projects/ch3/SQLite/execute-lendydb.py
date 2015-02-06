__author__ = 'Stuart'

"""
any time there is a print, if in console don't print
it would just return normally
"""

import lendydata as ld
ld.initDB()
print(ld.get_members())
print(ld.get_items())

ld.insert_item('Python Projects','Book',6,30,'Excellent')
###
# this should not have worked..... BUT IT DID. WTF PRAGMA?!>!?
###

ld.insert_member('Alan','alan@emailaddress.com')
print(ld.get_members())
ld.insert_item('Python Projects','Book',6,30,'Excellent')
ld.get_items()

ld.update_item(7,Price=25)
ld.get_item_details(7)
ld.get_member_name(6)
ld.update_member(6,Name='Alan Gould')
ld.get_member_details(6)

ld.delete_member(6)  # this also shouldn't work due to referential integrity, but does...
ld.delete_item(7)
ld.delete_member(6)

ld.cursor.execute("""
    select * from item
    where OwnerID in (select id from member where name like '%e%')
    """).fetchall()

ld.cursor.execute("""
    select * from item
    where ownerid not in (select id from member where name like '%e%')
    """).fetchall()

ld.get_member_name(4)

ld.closeDB()  # gotta close or else it won't save any of the changes