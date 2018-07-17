import sqlite3
from flask_restful import Resource, reqparse

from models.user import UserModel

# the User() class moved to models package

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
		user_check = UserModel.find_by_username(data['username'])
		if user_check:
			return {"message":"User {} has already register.".format(user_check.username)}, 400

		# the sqlite3 lib
		# connection = sqlite3.connect('data.db')
		# cursor = connection.cursor()
		
		# # this is an odd behavior of sqlite auto_incrementing values
		# #    the parameter must be 'NULL'
		# sql_insert_user = "INSERT INTO users VALUES (NULL, ?, ?)"
		# cursor.execute(sql_insert_user,(data['username'], data['password']))

		# connection.commit()
		# connection.close()

		# now with orm sqlalchemy (3 ways that work)
		# user = UserModel(None,data['username'], data['password'])
		# user = UserModel(userid=None, username=data['username'], password=data['password'])
		user = UserModel(userid=None, **data)
		try:
			user.save_user()
		except:
			return {"message":"Error, unable to complete request."}, 500
		return {"message":"User {} has been registered".format(user.username)}, 201