from flask_restful import Resource, Api
from flask import Flask

# having issues getting this module to import
# odd behavior:
# python app.py   # this doesn't run with a module flask_restful not found
# python3 app.py  # this does run

app = Flask(__name__)
api = Api(app)

class Student(Resource):
	def get(self,name):
		return {'student': name}

api.add_resource(Student, '/student/<string:name>')

app.run(host='10.0.2.15',port='58080')
