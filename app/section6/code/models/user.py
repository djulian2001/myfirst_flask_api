import sqlite3
from db import db

# the instructor said to change this to UserModel.  I'm not sure I see
# why he did this or is naming things this way.  I'm going to leave it
# until I understand why...
# class UserModel():
class UserModel(db.Model):
	"""docstring for User"""
	__tablename__ = 'users'
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(79))
	password = db.Column(db.String(79))

	def __init__(self, userid, username, password):
		self.id = userid
		self.username = username
		self.password = password
	
	def save_user(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def find_by_username(cls, username):
		# connection = sqlite3.connect('data.db')
		# cursor = connection.cursor()

		# query = "SELECT * FROM users WHERE username=?"
		# result = cursor.execute(query, (username,))
		# row = result.fetchone()
		# if row:
		# 	# example of just row pointers
		# 	# user = cls(row[0],row[1],row[2])
		# 	# example of setting name attributes
		# 	# user = cls(userid=row[0],username=row[1],password=row[2])
		# 	# another way?
		# 	user = cls(*row)
		# else:
		# 	user = None

		# connection.close()
		# return user
		return cls.query.filter_by(username=username).first()

	@classmethod
	def find_by_id(cls,userid):
		# connection = sqlite3.connect('data.db')
		# cursor = connection.cursor()

		# query = "SELECT * FROM users WHERE id=?"
		# result = cursor.execute(query, (id,))
		# row = result.fetchone()
		# if row:
		# 	# example of just row pointers
		# 	# user = cls(row[0],row[1],row[2])
		# 	# example of setting name attributes
		# 	# user = cls(userid=row[0],username=row[1],password=row[2])
		# 	# another way?
		# 	user = cls(*row)
		# else:
		# 	user = None

		# connection.close()
		# return user
		return cls.query.filter_by(id=userid).first()

