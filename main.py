import sqlite3
try:
    sqliteConnection = sqlite3.connect('b.db')
    sqlite_create_table_query = '''CREATE TABLE movies (
                                id INTEGER PRIMARY KEY,
                                name VARCHAR(30) NOT NULL,
                                directorname VARCHAR(30),
					   rating INTEGER);'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)

try:
    sqliteConnection = sqlite3.connect('b.db')
    cursor = sqliteConnection.cursor()

    sqlite_insert_query = """INSERT INTO movies(id, name, directorname, rating) VALUES(1,"padmavat","sanjay leela bansali",4);"""
    count = cursor.execute(sqlite_insert_query)
    A = """INSERT INTO movies(id, name, directorname, rating) VALUES(2,"bahubali","rajmouli",4);"""
    count = cursor.execute(A)
    B = """INSERT INTO movies(id, name, directorname, rating) VALUES(3,"kgf","PRASHANTH",5);"""
    count = cursor.execute(B)
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)


def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('b.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from movies"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for row in records:
            print("Id: ", row[0])
            print("Name: ", row[1])
            print("Director name: ", row[2])
            print("Rating: ", row[3])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


readSqliteTable()