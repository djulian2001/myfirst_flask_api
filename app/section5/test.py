import sqlite3

# init a connection
# this will create a file here? relative path?
connection = sqlite3.connect('data.db')

# this is line the engine object in sqlalchemy
# it will 'drive' our sql statements into the db (data.db)
cursor = connection.cursor()

table_check = "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
if not cursor.execute(table_check):
	# make a variable with a create table statement
	create_users_table = "CREATE TABLE users (id int, username text, password text)"

	# this will add the table...
	cursor.execute(create_users_table)

users =[ (1, 'jose', 'asdf'),
 		(1, 'jose', 'asdf'),
 		(1, 'jose', 'asdf'),]

user_inserts = "INSERT INTO users VALUES (?, ?, ?)"
# so there is this pattern 
for user in users:
	cursor.execute(user_inserts,user)

# but sqlite3 module has a method to do many inserts
users2 =[ (2, 'bob', 'asdf'),
 		(2, 'bob', 'asdf'),
 		(2, 'bob', 'asdf'),]

cursor.executemany(user_inserts, users2)

connection.commit()


# now lets get data out of our database
select_users = "SELECT id, username, password FROM users"

# 2 different ways
rows = cursor.execute(select_users)
for row in rows:
	print(row)

for row in cursor.execute(select_users):
	print(row)

connection.close()
