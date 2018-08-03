import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# The auto_incrementing primary key requires this syntax
# INTEGER PRIMARY KEY
sql_create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"

cursor.execute(sql_create_table)

sql_create_table = "CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY, name text, price real)"

cursor.execute(sql_create_table)

sql_create_table = "CREATE TABLE IF NOT EXISTS store (id INTEGER PRIMARY KEY, name text, location text)"

cursor.execute(sql_create_table)

sql_create_table = "CREATE TABLE IF NOT EXISTS inventory (id INTEGER PRIMARY KEY, store_id INTEGER REFERENCES store (id) ON DELETE RESTRICT ON UPDATE CASCADE, item_id INTEGER REFERENCES item (id) ON DELETE RESTRICT ON UPDATE CASCADE, quantity INTEGER DEFAULT 0, mark_down INTEGER DEFAULT 0)"

cursor.execute(sql_create_table)

cursor.execute("INSERT INTO store VALUES(NULL,'test_store','test street')")
# seed some test data
cursor.execute("INSERT INTO item VALUES(NULL,'test_book',99.99),(NULL,'test_chair',199.99)")
cursor.execute("INSERT INTO inventory VALUES(NULL,1,2,99,99),(NULL,2,2,1,2)")


connection.commit()
connection.close()
