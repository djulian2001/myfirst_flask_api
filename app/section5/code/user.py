import sqlite3
from flask_restful import Resource, reqparse

class User():
	"""docstring for User"""
	def __init__(self, userid, username, password):
		self.id = userid
		self.username = username
		self.password = password
	
	@classmethod
	def find_by_username(cls, username):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "SELECT * FROM users WHERE username=?"
		result = cursor.execute(query, (username,))
		row = result.fetchone()
		if row:
			# example of just row pointers
			# user = cls(row[0],row[1],row[2])
			# example of setting name attributes
			# user = cls(userid=row[0],username=row[1],password=row[2])
			# another way?
			user = cls(*row)
		else:
			user = None

		connection.close()
		return user

	@classmethod
	def find_by_id(cls,id):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "SELECT * FROM users WHERE id=?"
		result = cursor.execute(query, (id,))
		row = result.fetchone()
		if row:
			# example of just row pointers
			# user = cls(row[0],row[1],row[2])
			# example of setting name attributes
			# user = cls(userid=row[0],username=row[1],password=row[2])
			# another way?
			user = cls(*row)
		else:
			user = None

		connection.close()
		return user


# the mapping to this class to the url is done in the app.py
# with line api.add_resource(UserRegister, '/register')
class UserRegister(Resource):
	"""validating input data using reqparse"""
	user_parser = reqparse.RequestParser()
	user_parser.add_argument(
		'username',
		type=str,
		required=True,
		help="User name is a required value." )
	user_parser.add_argument(
		'password',
		type=str,
		required=True,
		help="User password is a required value.")

	"""has a post method defined as part of the flask_restful.Resource"""	
	def post(self):
		# instructor had
		# data = UserRegister.user_parser.parse_args()
		data = self.user_parser.parse_args()
		
		# using the User method find_by_username to check if the user exists
		user_check = User.find_by_username(data['username'])
		if user_check:
			return {"message":"User {} has already register.".format(user_check.username)}, 400

		# the sqlite3 lib
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()
		
		# this is an odd behavior of sqlite auto_incrementing values
		#    the parameter must be 'NULL'
		sql_insert_user = "INSERT INTO users VALUES (NULL, ?, ?)"
		cursor.execute(sql_insert_user,(data['username'], data['password']))

		connection.commit()
		connection.close()

		return {"message":"User has been registered"}, 201