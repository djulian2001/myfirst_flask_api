from flask_restful import Resource, Api, reqparse
from flask import Flask, request
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
# python3 app.py  # this does run

app = Flask(__name__)
api = Api(app)

# this is a secret, required and must be set, probably in a config file
app.secret_key = 'donotmakepublic'

# the json web token, JWT, help(JWT)
# __init__(self, app=None, authentication_handler=None, identity_handler=None)

jwt = JWT(app, authenticate, identity)

# storage (in memory database)
items = []

class Item(Resource):
	def find_item(self, name):
		"""
			This method is used to find an item by name in the database
			returns the item or none
		"""
		return next(filter(lambda item: item['name'] == name, items), None)

	def validate_data_request(self):
		parser = reqparse.RequestParser()
		parser.add_argument(
			'price',
			type = float,
			required = True,
			help = "Null value, this field is required." )

		return parser.parse_args()

	@jwt_required()
	def get(self, name):
		item = self.find_item(name)
		return {'item': item}, 200 if item else 404
	
	@jwt_required()
	def post(self, name):
		item_check = self.find_item(name)
		if item_check:
			return {'message':'Found existing item {}.'.format(item_check['name'])}, 400
		
		data = self.validate_data_request()
		# data = request.get_json() 
			# ways to deal with request payloads (content-type = application/json)
			# force=True  # deal with the junk data
			# silent=True # return null but not an error

		item = {'name': name, 'price': data['price']}
		items.append(item)

		return item, 201
	
	@jwt_required()
	def delete(self, name):
		item_check = self.find_item(name)
		if item_check is None:
			return {'message':'Item {} does not exist.'.format(name)}, 400

		global items
		items = list(filter(lambda item: item['name'] != name, items))
		return {'message':'Item {} has been deleted.'.format(name)}, 200

	@jwt_required()
	def put(self, name):
		data = self.validate_data_request()

		item = self.find_item(name)
		if item:
			item.update(data)
		else:
			item = {'name': name, 'price': data['price']}
			items.append(item)
		return item, 200


class Items(Resource):
	@jwt_required()
	def get(self):
		return {'items': items}, 202


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

app.run(host='10.0.2.15', port='58080', debug=True)
