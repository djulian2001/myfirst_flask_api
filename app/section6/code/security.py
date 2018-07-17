from werkzeug.security import safe_str_cmp
from models.user import UserModel

# interesting uni-code is python3 so == is safe?
# but in python 2.7 == is not safe, so use the module werkzeug.security

# users = [
# 	User(userid=1, username='bob', password='asdf'),
# 	User(userid=2, username='sam', password='1234'),
# 	User(userid=3, username='tim', password='qwer'),
# ]
# above is replaced with ../data.db database

# make indexes for username and id
# username_mapping = {
# 	'bob':{'id':1,'username':'bob','password':'asdf'},
# 	'sam':{'id':2,'username':'sam','password':'1234'},
# 	'tim':{'id':3,'username':'tim','password':'qwer'},
# }
# with set comprehension the above becomes...
# username_mapping = {user.username: user for user in users}
# above is removed by the User.find_by_username class method

# userid_mapping = {
# 	1:{'id':1,'username':'bob','password':'asdf'},
# 	2:{'id':2,'username':'sam','password':'1234'},
# 	3:{'id':3,'username':'tim','password':'qwer'},	
# }
# with set comprehension the above becomes...
# userid_mapping = {user.id: user for user in users}
# above is removed by the User.find_by_id class method

def authenticate(username, password):
	# user = username_mapping.get(username, None)
	user = UserModel.find_by_username(username)
	# if user and user.password == password:   			# python3 safe
	if user and safe_str_cmp(user.password, password):  # safer in many places
		return user

def identity(payload):
	user_id = payload['identity']
	# return userid_mapping.get(user_id, None)
	return UserModel.find_by_id(user_id)