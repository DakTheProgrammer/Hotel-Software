import sqlite3
import json
import csv
import random

con = sqlite3.connect('SQLite\Databases\Hotel.sqlite')
cur = con.cursor()

def loadUsers():
    with open('../MockData/MockUser.json') as f:
        file = json.load(f)

    query = 'INSERT INTO Guest (%s) VALUES({row})'

    for row in file:
        query = f'INSERT INTO Users (Username, Password, First, Last, Email, Type) VALUES{row["Username"], row["Password"], row["First"], row["Last"], row["Email"], row["Type"]}'
        cur.execute(query)
        con.commit()

def loadEmployee():
    query = 'SELECT * FROM Users'
    cur.execute(query)
    con.commit()

    users = cur.fetchall()

    for user in users:
        if user[5] != 'Guest':
            print(user)
            query = f'INSERT INTO Employee (Username, First, Last, Role, Status) VALUES{user[0], user[2], user[3], user[5], False}'
            cur.execute(query)
            con.commit()
    
def loadGuests():
    query = 'SELECT * FROM Users'
    cur.execute(query)
    con.commit()

    users = cur.fetchall()

    types = ['Basic', 'Bronze', 'Silver', 'Gold', 'Platinum']

    for user in users:
        if user[5] == 'Guest':
            query = f'UPDATE Guest SET (Username, First, Last, Member, Cart, Balance) = {user[0], user[2], user[3], types[random.randint(0,4)], "Empty", 0} WHERE Username = "{user[0]}"'
            cur.execute(query)
            con.commit()

def loadRooms():
    query = 'SELECT * FROM Guest'
    cur.execute(query)
    con.commit()

    users = cur.fetchall()

    bools = [True, False]
    status = ['cleaned', 'dirty']
    oc = ['occupied', 'open', 'unknown']

    room = 100

    for i in range(41):
        query = f'INSERT INTO Room (Room, Username, First, Last, Checked, Status, Occupancy) VALUES{room, "Empty", "Empty", "Empty", False, "Empty", "Empty"}'
        cur.execute(query)
        con.commit()

        room += 1

    room = 200

    for user in users:
        query = f'INSERT INTO Room (Room, Username, First, Last, Checked, Status, Occupancy) VALUES{room, user[0], user[1], user[2], bools[random.randint(0,1)], status[random.randint(0,1)], oc[random.randint(0,2)]}'
        cur.execute(query)
        con.commit()

        if str(room)[-2:] == '40':
            room += 60
        else:
            room += 1

def loadBags():
    query = 'SELECT * FROM Room'
    cur.execute(query)
    con.commit()

    users = cur.fetchall()

    for user in users:
        if user[1] != 'Empty':
            query = f'INSERT INTO Bags (Username, First, Last, Room, Status, Location, Request) VALUES{user[1], user[2], user[3], user[0], "Taken", "None", False}'
            cur.execute(query)
            con.commit()
        
def loadMenu():
    with open('MockData/InternetItems.csv') as f:
        items = list(csv.reader(f))

    for row in items:
        query = f'INSERT INTO Menu (Name, Type, SubType, Description, Price, Amount) VALUES{row[0], row[1], row[2], row[3], row[4], row[5]}'
        cur.execute(query)
        con.commit()

def loadMessages():
    table = """CREATE TABLE Messages(
    Username varchar(255) NOT NULL,
    Message varchar(600) NOT NULL,
    PRIMARY KEY(Username)
    );"""

    cur.execute(table)

    query = 'SELECT Username FROM Employee'
    cur.execute(query)
    con.commit()

    users = cur.fetchall()
    for row in users:
        query = f'Insert INTO Messages (Username, Message) VALUES {row[0], "None"}'
        cur.execute(query)
        con.commit()

def loadMessages():
    cur.execute("DROP TABLE Messages")

    table = """CREATE TABLE Messages(
    Username varchar(255) NOT NULL,
    Message varchar(600) NOT NULL,
    PRIMARY KEY(Username)
    );"""

    cur.execute(table)

    query = 'SELECT Username FROM Employee'
    cur.execute(query)
    con.commit()

    users = cur.fetchall()
    for row in users:
        query = f'Insert INTO Messages (Username, Message) VALUES {row[0], "None"}'
        cur.execute(query)
        con.commit()

import sys;
print(sys.version)

print(
'''1: Load Users
2: Load Employee
3: Load Guests
4: Load Rooms
5: Load Bags
6: Load Menu
7: Load Messages''')
sel = int(input())
match sel:
    case 1:
        loadUsers()
    case 2:
        loadEmployee()
    case 3:
        loadGuests()
    case 4:
        loadRooms()
    case 5:
        loadBags()
    case 6:
        loadMenu()
    case 7:
        loadMessages()
    case _:
        print('you are an idiot')
