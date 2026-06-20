# Import the sqlite3 module to work with SQLite databases
import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("my_database.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create a table 
cursor.execute(
    "CREATE TABLE green_pledge (id INTEGER, name TEXT)"
)

# Commit the changes and close the connection
connection.commit()
connection.close()