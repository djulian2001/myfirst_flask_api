from flask_restful import Api
from flask import Flask
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, Items

# python3 app.py  # this does run

app = Flask(__name__)
api = Api(app)

# this is a secret, required and must be set, probably in a config file
app.secret_key = 'donotmakepublic'

# the json web token, JWT, help(JWT)
# __init__(self, app=None, authentication_handler=None, identity_handler=None)

jwt = JWT(app, authenticate, identity)

# storage (in memory database)
# items = [] # replaced with a sqlite3 database

# in lecture 69 moved item into item.py

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')

app.run(host='10.0.2.15', port='58080', debug=True)
