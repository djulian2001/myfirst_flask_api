import sqlite3, json
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
	def find_item(self, name):
		"""
			This method is used to find an item by name in the database
			returns the item or none
		"""
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()
		sql_item = "SELECT * FROM items WHERE name = ?"

		row = cursor.execute(sql_item, (name,)).fetchone()
		# above is cleaner than:
		# rows = cursor.execute(sql_item, (name,))
		# row = rows.fetchone()
		#print(type(row)) <class 'tuple'>
		if row:
			# this converts the tuple to a list
			# return json.dumps(row)
			# vs
			return {'id':row[0],'name':row[1],'price':row[2]}
		return None

		# return next(filter(lambda item: item['name'] == name, items), None)

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
		# when using an in memory database
		# lets see if we can swap out the storage without changing this method
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

