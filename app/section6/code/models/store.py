from db import db

inventory_table = db.Table(
	'inventory',
	db.Column('id', db.Integer, primary_key=True),
	db.Column('store_id', db.Integer, db.ForeignKey('store.id')),
	db.Column('item_id', db.Integer, db.ForeignKey('item.id')),
	db.Column('quantity', db.Integer),
	db.Column('mark_down', db.Integer, default=0),)

class StoreModel(db.Model):
	"""
		Store should be a many to many with ItemModel.
		Base class is provided by the frame work.  Same concept as sqlalchemy
			- db.Model
		
		DB notes:  flavor? but plural for stores table name, is ? others say 'store'

		code thought:
		What if i created a core class say:
			class CoreClassAPI(object):
				def json(self):
				def find(cls,string):
				def save(self):
				def insert(self):
				def delete(self):
				def update(self):
			The class could be inherited by the model, providing less code
	"""
	__tablename__ = 'store'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(79))
	location = db.Column(db.String(23))
	items = db.relationship("ItemModel", secondary=inventory_table, back_populates="stores")
	
	def __init__(self, name, location):
		self.name = name
		self.location = location

	# helper methods
	def json(self):
		return {'id':self.id,'name':self.name,'location':self.location}

	def save_store(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def find_store(cls, find_name):
		"""
			This method takes in a string and returns a store object or none
		"""
		return cls.query.filter_by(name=find_name).first()

	def update_store(self):
		self.save_store()

	def insert_store(self):
		self.save_store()

	def delete_store(self):
		db.session.delete(self)
		db.session.commit()
