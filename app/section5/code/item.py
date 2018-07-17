import sqlite3, json
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
	item_parser = reqparse.RequestParser()
	# item_parser.add_argument(
	# 	'name',
	# 	type = str,
	# 	required = True,
	# 	help = "Null value, this is a required field.")
	item_parser.add_argument(
		'price',
		type = float,
		required = True,
		help = "Null value, this is a required field." )

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
		connection.close()
		if row:
			# this converts the tuple to a list
			# return json.dumps(row)
			# vs
			return {'id':row[0],'name':row[1],'price':row[2]}
		return None

		# return next(filter(lambda item: item['name'] == name, items), None)

	def insert_item(self, name, price):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()
		sql_insert_item = "INSERT INTO items (name,price) VALUES (?, ?)"

		cursor.execute(sql_insert_item, (name, price,))
		connection.commit()
		connection.close()


	@jwt_required()
	def get(self, name):
		# when using an in memory database
		# lets see if we can swap out the storage without changing this method
		item = self.find_item(name)
		return {'item': item}, 200 if item else 404
	
	@jwt_required()
	def post(self, name):
		
		data = self.item_parser.parse_args()
		# data = request.get_json() 
			# ways to deal with request payloads (content-type = application/json)
			# force=True  # deal with the junk data
			# silent=True # return null but not an error

		item_check = self.find_item(name)
		if item_check:
			return {'message':'Found existing item {}.'.format(item_check['name'])}, 400
		
		try:
			self.insert_item(name, data['price'])
		except:
			return {'message':'Error, failed to add item {}'.format(name)}, 500
		
		return {'message':'Item {} added.'.format(name)}, 201
	
	@jwt_required()
	def delete(self, name):
		# item_check = self.find_item(name)
		# if item_check is None:
		# 	return {'message':'Item {} does not exist.'.format(name)}, 400

		# global items
		# items = list(filter(lambda item: item['name'] != name, items))
		# return {'message':'Item {} has been deleted.'.format(name)}, 200

		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		sql_delete_item = "DELETE FROM items WHERE name = ?"

		cursor.execute(sql_delete_item, (name,))
		connection.commit()
		connection.close()
		return {'message':'Item {} has been deleted.'.format(name)}, 200

	@jwt_required()
	def put(self, name):
		data = self.item_parser.parse_args()

		item = self.find_item(name)
		if item:
			try:
				self.update_item(item)
			except:
				return {'message':'Error, failed to update item {}'.format(item['name'])}, 500
			return {'message':'Item {} updated to price {}.'.format(item['name'],item['price'])}, 201
		else:
			try:
				self.insert_item(name, data['price'])
			except:
				return {'message':'Error, failed to add item {}'.format(name)}, 500
			return {'message':'Item {} added.'.format(name)}, 201

	def update_item(self, item):
		sql_update_item = "UPDATE items SET price = ? WHERE name = ?"
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()
		cursor.execute(sql_update_item, (item['price'],item['name'],))
		connection.commit()
		connection.close()


class Items(Resource):
	@jwt_required()
	def get(self):
		sql_items = "SELECT name, price FROM items"
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()
		rows = cursor.execute(sql_items)
		
		# items_list = [ {row['name']: row['price']} for row in rows ]
		items_list = [ {'name':row[0],'price':row[1]} for row in rows ]
		connection.close()
		return {'items': items_list}, 202
		

