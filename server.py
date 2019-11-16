# Imports
from flask import Flask, request, jsonify, current_app
import pymongo
from bson.objectid import ObjectId
import os
import json

# Define app variable
app = Flask(__name__)

# Define database
myclient = pymongo.MongoClient(os.getenv('MONGODB_URI', "mongodb://localhost:27017"))
database = myclient[(os.getenv('MONGODB_NAME', "flask102"))]
collection = database["wines"]

# Send the home page
@app.route('/', methods=['GET'])
def sendHTMLFile():
    return current_app.send_static_file('index.html')

# Send all records back in an array
@app.route('/api/all', methods=['GET'])
def test_json2():
    data = collection.find().sort('name')
    arr = []
    for item in data:
      arr.append(item)
    return json.dumps(arr, default=str)

# Send as url params the key and value to search for
@app.route('/api/query', methods=['GET'])
def test_json3():
    x = request.args.get('key')
    y = request.args.get('value')
    myquery = { x: y }
    data = collection.find(myquery)
    arr = []
    for item in data:
      arr.append(item)
    return json.dumps(arr, default=str)

# Send as an object to add new
@app.route('/api', methods=['POST'])
def addRecord():
    request.json['isFavorite'] = False
    collection.insert_one(request.json)
    return jsonify(
      code=0,
      msg="Success"
    )

# Send as object containing a find object and a replace object to update
@app.route('/api', methods=['PUT'])
def updateRecord():
    myquery = {'_id': ObjectId(request.json['_id'])}
    newvalues = { "$set": {'isFavorite': request.json['isFavorite'] } }
    collection.update_one(myquery, newvalues)
    return jsonify(
      code=0,
      msg="Success"
    )

# Send as object the criteria to determine which record should be deleted
@app.route('/api', methods=['DELETE'])
def deleteRecord():
    print({'_id': request.json['_id']})
    collection.delete_one({'_id': ObjectId(request.json['_id'])})
    return jsonify(
      code=0,
      msg="Success"
    )

# Start server listening
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)