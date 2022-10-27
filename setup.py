import sqlite3

# DB-API spec for talking to relational databases in Python

connection = sqlite3.connect("games.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table games")
except:
    pass


cursor.execute("create table games (id integer primary key, name text)")

cursor.execute("insert into games (name) values ('cricket')")
cursor.execute("insert into games (name) values ('football')")
cursor.execute("insert into games (name) values ('hockey')")
cursor.execute("insert into games (name) values ('soccer')")
cursor.execute("insert into games (name) values ('basketball')")

connection.commit()
connection.close()

print("completed")