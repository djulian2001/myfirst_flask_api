from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel

class Item(Resource):
	"""
		'resources' are public api facing code
			contents of this ./resources packages are imported
			from flask_restful import Resource
			and mixed into the class
			like this class Item(Resource):

		This layer needs to talk HTML and JSON to the client.
			another way the instructor represnted this package was as
			resources used by the clients, the public api code.
		
		This are the public api 'end points' for the client
	"""
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

# MOVED TO section6/models/item.py Item class
	# def update_item(self, item):
	# 	sql_update_item = "UPDATE items SET price = ? WHERE name = ?"
	# 	connection = sqlite3.connect('data.db')
	# 	cursor = connection.cursor()
	# 	cursor.execute(sql_update_item, (item['price'],item['name'],))
	# 	connection.commit()
	# 	connection.close()

	# def find_item(self, name):
	# 	"""
	# 		This method is used to find an item by name in the database
	# 		returns the item or none
	# 	"""
	# 	connection = sqlite3.connect('data.db')
	# 	cursor = connection.cursor()
	# 	sql_item = "SELECT * FROM items WHERE name = ?"

	# 	row = cursor.execute(sql_item, (name,)).fetchone()
	# 	# above is cleaner than:
	# 	# rows = cursor.execute(sql_item, (name,))
	# 	# row = rows.fetchone()
	# 	#print(type(row)) <class 'tuple'>
	# 	connection.close()
	# 	if row:
	# 		# this converts the tuple to a list
	# 		# return json.dumps(row)
	# 		# vs
	# 		return {'id':row[0],'name':row[1],'price':row[2]}
	# 	return None

	# 	# return next(filter(lambda item: item['name'] == name, items), None)

	# def insert_item(self, name, price):
	# 	connection = sqlite3.connect('data.db')
	# 	cursor = connection.cursor()
	# 	sql_insert_item = "INSERT INTO items (name,price) VALUES (?, ?)"

	# 	cursor.execute(sql_insert_item, (name, price,))
	# 	connection.commit()
	# 	connection.close()

	@jwt_required()
	def get(self, name):
		# when using an in memory database
		# lets see if we can swap out the storage without changing this method
		item = ItemModel.find_item(name)
		if item:
			return {'item': item.json()}, 200 
		return {'message':'Item {} not found'.format(name)},404
	
	@jwt_required()
	def post(self, name):
		
		data = self.item_parser.parse_args()
		# data = request.get_json() 
			# ways to deal with request payloads (content-type = application/json)
			# force=True  # deal with the junk data
			# silent=True # return null but not an error

		item_check = ItemModel.find_item(name)
		if item_check:
			return {'message':'Found existing item {}.'.format(item_check.name)}, 400
		
		try:
			item = ItemModel(name, data['price'])
			item.insert_item()
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
		item = ItemModel.find_item(name)
		if item:
			try:
				item.delete_item()			
			except:
				return {'message':'Internal issue unable to complete request.'}, 500
			return {'message':'Item {} has been deleted.'.format(name)}, 200
		return {'message':'Item {} does not exist to delete.'.format(name)}, 400

		# moved to the ItemModel
		# connection = sqlite3.connect('data.db')
		# cursor = connection.cursor()

		# sql_delete_item = "DELETE FROM items WHERE name = ?"

		# cursor.execute(sql_delete_item, (name,))
		# connection.commit()
		# connection.close()
		

	@jwt_required()
	def put(self, name):
		"""
			Interesting, arg 'name' is a public value, aka should be projected from change
			test: changed to find_name and broke code with error:
				TypeError: put() got an unexpected keyword argument 'name'
		"""
		data = self.item_parser.parse_args()

		item = ItemModel.find_item(name)

		if item:
			item.price = data['price']
			event="updated"
		else:
			item = ItemModel(name, data['price'])
			event="inserted"

		try:
			item.save_item()
		except:
			return {'message':'Error, item {} failed to be {}!'.format(event, name)}, 500
		return {'message':'Item {} {} to price {}.'.format(item.name, event, item.price)}, 201


class Items(Resource):
	@jwt_required()
	def get(self):
		# sql_items = "SELECT name, price FROM items"
		# connection = sqlite3.connect('data.db')
		# cursor = connection.cursor()
		# rows = cursor.execute(sql_items)
		# items_list = [ {row['name']: row['price']} for row in rows ]
		# items_list = [ {'name':row[0],'price':row[1]} for row in rows ]
		# connection.close()
		items_list = ItemModel.query.all()
		if items_list:
			# with list comprehension
			# return {'items': [item.json() for item in items_list] }, 202
			# with lambda function
			return {'items': list(map(lambda x: x.json(), items_list))}, 202
		return {'message':'No item records found.'}, 404

