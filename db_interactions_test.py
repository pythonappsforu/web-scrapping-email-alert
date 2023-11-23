import sqlite3

'''Establish a connection and cursor'''
connection = sqlite3.Connection("data.db")
cursor = connection.cursor()

# select columns based on condition
cursor.execute("SELECT band,date FROM events WHERE city='Tiger city'")
print(cursor.fetchall())

# insert values into table
new_rows = [('leopard','Leopard city','14.10.2000'),
            ('cat','cat city','12.10.2000')]
cursor.executemany("INSERT INTO events VALUES(?,?,?)",new_rows)
connection.commit()

# fetch all data
cursor.execute("SELECT * FROM events")
print(cursor.fetchall())