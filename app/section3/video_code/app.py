from flask import Flask, jsonify, request, render_template

# unique place
app = Flask(__name__)

# storage
stores = [
	{ 'name': 'My coffee shop','items': [
			{'name': 'cool beans','price': 12.11},
			{'name': 'extra strong','price': 13.99}, ] },
	{ 'name': 'My hot dog stand','items':[ 
			{'name':'beef frank','price':2.99},
			{'name':'beer pork','price':3.49}, ] },
]


# requests the app can understand

@app.route('/') # what does this look like http://www.app.my_domain.com
def home():
	return render_template('index.html')

# we are a server... not a browser
# post - used to receive data
# get - used to send data back only

# post /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
	request_data = request.get_json()
	new_store = {
		'name': request_data['name'],
		'items': []
	}
	# add state to storage
	stores.append(new_store)
	# response in json format
	return jsonify(new_store)

# get /store/<string:name>  # this is a flask string is the data type and name is variable
@app.route('/store/<string:name>')
def get_a_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify(store)
	return jsonify({'message':'store not found'})

# get /store
@app.route('/store')
def get_stores():
	return jsonify({'stores': stores})

# post /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
	request_data = request.get_json()
	new_item = {'name': request_data['name'], 'price': request_data['price']}
	for store in stores:
		if store['name'] == name:
			store['items'].append(new_item)
			return jsonify(new_item)
	return jsonify({'message':'store not found'})

# get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify({'items': store['items']})
	return jsonify({'message':'items not found'})


app.run(host="10.0.2.15", port=58080)
# with vagrant, http://localhost:8080
