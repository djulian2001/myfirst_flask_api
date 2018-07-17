import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# The auto_incrementing primary key requires this syntax
# INTEGER PRIMARY KEY
sql_create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"

cursor.execute(sql_create_table)

sql_create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"

cursor.execute(sql_create_table)

# seed some test data
cursor.execute("INSERT INTO items VALUES(NULL,'test_book',99.99),(NULL,'test_chair',199.99)")

connection.commit()
connection.close()
