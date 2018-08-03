from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.store import StoreModel

class Store(Resource):
	"""
		The public api for getting store information
	"""

	store_parser = reqparse.RequestParser()

	store_parser.add_argument(
		'location',
		type = str,
		required = True,
		help = "Null value, this store requires a location.")

	# @jwt_required()
	def get(self, name):
		store = StoreModel.find_store(name)
		if store:
			return {'store':store.json()}, 200
		return {'message':'Store {} not found.'.format(name)}, 404

	@jwt_required()
	def post(self, name):
		# add location to payload
		data = self.store_parser.parse_args()
		store_check = StoreModel.find_store(name)
		if store_check:
			return {'message':'Store {} already exists.'.format(name)}, 400

		try:
			store = StoreModel(name=name,location=data['location'])
			store.insert_store()
		except:
			# in a real system I would need to log the Exception in addition to sending a response 
			return {'message':'Error, failed to add the store {}'.format(name)}, 500
		return {'message':'Store {} has been added.'.format(store.name)}, 201

	@jwt_required()
	def delete(self, name):
		store = StoreModel.find_store(name)
		if store:
			try:
				store.delete_store()
			except:
				return {'message':'Error, failed to remove the store {}'.format(name)}, 500
			return {'message':'Store {} has been removed'.format(store.name)}, 200
		return {'message':'Store {} does not exist to remove.'.format(name)}, 400

	@jwt_required()
	def put(self, name):
		data = self.store_parser.parse_args()
		store = StoreModel.find_store(name)
		if store:
			store.location = data['location']
			event="updated"
		else:
			store = StoreModel(name=name, location=data['location'])
			event="inserted"

		try:
			store.save_store()
		except:
			return {'message':'Error, store {} failed to be {}.'.format(name, event)}, 500
		return {'message':'Store {} {} to location {}.'.fromat(store.name, event, store.location)}, 201

class Stores(Resource):
	def get(self):
		store_list = StoreModel.query.all()
		if store_list:
			return {'stores': list(map(lambda x: x.json(), store_list))}, 202
		return {'message':'No store records found.'}, 404

class StoreInventory(Resource):
	def get(self,name):
		store = StoreModel.find_store(name)
		if store:
			# return {'id':store.id,'name':store.name,'location':store.location,'inventory':[item.json() for item in store.items]}, 202
			return {'store':store.json(),'inventory':[item.json() for item in store.items]}, 202
