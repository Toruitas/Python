__author__ = 'Stuart'

"""
lending library database API

Provides a CRUD interface to item and member entities
and init and close functions for database control.
"""

import sqlite3 as sql
db = None
cursor = None

####CRUD functions for items ####

def insert_item(Name, Description, OwnerID, Price, Condition):
    query = """
        insert into item
        (Name, Description, OwnerID, Price, Condition, DateRegistered)
        values (?,?,?,?,?,date('now'))"""  # date 'now' does what you think
    cursor.execute(query,(Name,Description,OwnerID,Price,Condition))

def get_items():
    query="""
        select ID, Name, Description, OwnerID, Price, Condition, DateRegistered
        from item"""
    return cursor.execute(query).fetchall()  # fetchall returns list of all matching queries

def get_item_details(id):
    query = """
        select Name, Description, OwnerID, Price, Condition, DateRegistered
        from item
        where id = ?"""
    return cursor.execute(query,(id,)).fetchall()[0]

def get_item_name(id):
    return get_item_details(id)[0]

def update_item(id, Name=None,Description=None,OwnerID=None,Price=None,Condition=None):
    query = """
        update item
        set Name=?, Description=?,OwnerID=?,Price=?,Condition=?
        where id=?"""
    data = get_item_details(id)  # if not Name means if name = none
    if not Name: Name = data[0]  # thus preserving existing info
    if not Description: Description = data[1]
    if not OwnerID: OwnerID = data[2]
    if not Price: Price = data[3]
    if not Condition: Condition = data[4]

    cursor.execute(query,(Name,Description,OwnerID,Price,Condition,id))

def delete_item(id):
    query="""
        delete from item
        where id = ?"""
    cursor.execute(query,(id,))

#### CRUD functions for members ####

def insert_member(name,email):
    query = """
        insert into member(name,email)
        values (?,?)"""
    cursor.execute(query,(name,email))

def get_members():
    query = """
        select id, name, email
        from member"""
    return cursor.execute(query).fetchall()

def get_member_details(id):
    query = """
    select name, email
    from member
    where id = ?"""
    return cursor.execute(query,(id,)).fetchall()[0]

def get_member_name(id):
    return get_member_details(id)[0]

def update_member(id,Name=None,Email=None):
    """
    the params are None to enable user to simply update the one they need.
    if something is none, the data is preserved and entered into the new execution
    """
    query = """
        update member
        set name = ?, email=?
        where id=?"""
    data = get_member_details(id)
    if not Name: Name = data[0]
    if not Email: Email = data[1]
    cursor.execute(query,(Name,Email,id))

def delete_member(id):
    query = """
        delete from member
        where id = ?"""
    cursor.execute(query,(id,))

#### Database init and close ####
def initDB(filename = None):
    global db, cursor
    if not filename:
        filename = 'lendy.db'
    try:
        db = sql.connect(filename)
        cursor = db.cursor()
    except:
        print("Error connecting to", filename)
        cursor = None
        raise

def closeDB():
    try:
        cursor.close()
        db.commit()
        db.close()
    except:
        print("Problem closing database...")
        raise

if __name__ == "__main__":
    initDB()  # use default file
    print("Members:\n",get_members())
    print("Items:\n",get_items())