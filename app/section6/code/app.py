from flask_restful import Api
from flask import Flask, jsonify
from flask_jwt import JWT

from datetime import timedelta

# from security import authenticate, identity as identity_function
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Items

# python3 app.py  # this does run

app = Flask(__name__)
# a flag for turning off the flasks sqlalchemy extensions behavior only
#	and allows the sqlalchemy packages core behavior
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

# this is a secret, required and must be set, probably in a config file
app.secret_key = 'donotmakepublic'

# the json web token, JWT, help(JWT)
# tut_flask_api/docs/flask-jwt-guide.pdf
# configuration of the jwt
# app.config['JWT_AUTH_URL_RULE'] = '/login'

# creating the database tables upon first request
@app.before_first_request
def create_tables():
	db.create_all()


# __init__(self, app=None, authentication_handler=None, identity_handler=None)
jwt = JWT(app, authenticate, identity)
# jwt = JWT(app, authenticate, identity_function) # just an alias
# app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
# app.config['JWT_AUTH_USERNAME_KEY'] = 'email'

# @jwt.auth_response_handler
# def customized_responsde_handler(access_token, identity):
# 	# import jsonify module from flask 
# 	return jsonify({'access_token':access_token.decode('utf-8'),'user_id':identity.id})

# error_handler didn't work, following did:
# @jwt.jwt_error_handler
# def customized_error_handler(error):
# 	return jsonify({'message': error.description,'code': error.status_code,}), error.status_code
# storage (in memory database)
# items = [] # replaced with a sqlite3 database

# in lecture 69 moved item into item.py

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')



# interesting point.  This is our apps entry point, BUT if we want to
# 	import this app.py file for whatever reason, with out the if statement
#   the flask app on import will run the app.run() method and start the
#	flask service (not what you want on an import)
# python behavior the entry point is the __main__, so if users.py is run
#	via the command line it gets the meta name __main__
if __name__ == '__main__':
	# By putting the db import for the apps initialization of the database here,
	#	we are avoiding circular imports.
	#	for the package models, the modules will import db to build the schema.
	#	the author is putting each tables configuration into the class variables
	from db import db
	db.init_app(app)
	app.run(host='10.0.2.15', port='58080', debug=True)
