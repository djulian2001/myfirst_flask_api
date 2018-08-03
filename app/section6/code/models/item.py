# import sqlite3  # no longer required here
from db import db

from models.store import inventory_table

class ItemModel(db.Model):
	"""
		We talk python from this layer /models/*.py
		inherits base class from SQLAlchemy
			- db.Model
	"""
	__tablename__ = 'item'

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(79))
	price = db.Column(db.Float(precision=2))
	stores = db.relationship("StoreModel", secondary=inventory_table, back_populates="items")

	def __init__(self, name, price):
		# super(Item, self).__init__()
		self.name = name
		self.price = price

	def json(self):
		return {'id':self.id,'name':self.name,'price':self.price}

	@classmethod
	def find_item(cls, find_name):
		"""
			This method is used to find an item by name in the database
			returns the item or none
		"""
		# connection = sqlite3.connect('data.db')
		# cursor = connection.cursor()
		# sql_item = "SELECT name, price FROM items WHERE name = ?"

		# row = cursor.execute(sql_item, (find_name,)).fetchone()
		# # above is cleaner than:
		# # rows = cursor.execute(sql_item, (name,))
		# # row = rows.fetchone()
		# #print(type(row)) <class 'tuple'>
		# connection.close()
		# if row:
		# 	# this converts the tuple to a list
		# 	# return json.dumps(row)
		# 	# vs
		# 	# return {'id':row[0],'name':row[1],'price':row[2]} 
		# 	# because we talk python types now we return a new Item instance
		# 	return cls(name=row[0],price=row[1]) # verbose
		# 	# return cls(*row) # 'unpacking' but the select * is a poor choice
		# return None
		# return next(filter(lambda item: item['name'] == name, items), None) # section4 with in memory 'db'?
		# using the ORM's pow-waa
		return cls.query.filter_by(name=find_name).first()


	def update_item(self):
		"""
			The add method in the orm can replace this method
			lets pass all of the following to it.
		"""
		# sql_update_item = "UPDATE items SET price = ? WHERE name = ?"
		# connection = sqlite3.connect('data.db')
		# cursor = connection.cursor()
		# cursor.execute(sql_update_item, (self.price, self.name,))
		# connection.commit()
		# connection.close()
		self.save_item()

	def insert_item(self):
		"""
			The add method in the orm can replace this method
			lets pass all of the following to it.
		"""
		# connection = sqlite3.connect('data.db')
		# cursor = connection.cursor()
		# sql_insert_item = "INSERT INTO items (name,price) VALUES (?, ?)"

		# cursor.execute(sql_insert_item, (self.name, self.price,))
		# connection.commit()
		# connection.close()
		self.save_item()
		
	def save_item(self):
		db.session.add(self)
		db.session.commit()

	def delete_item(self):
		# connection = sqlite3.connect('data.db')
		# cursor = connection.cursor()

		# sql_delete_item = "DELETE FROM items WHERE name = ?"

		# cursor.execute(sql_delete_item, (self.name,))
		# connection.commit()
		# connection.close()
		db.session.delete(self)
		db.session.commit()
