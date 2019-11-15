# Imports
from flask import Flask, request, jsonify
import pymongo
import os
import json

# Define app variable
app = Flask(__name__)

# Define database
myclient = pymongo.MongoClient("mongodb://localhost:27017")
database = myclient["flask102"]
collection = database["wines"]

# Send the home page
@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Hello World</h1><p>Sent to you by a server running Flask.</p>"

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
    collection.insert_one(request.json)
    return "<p>Record added.</p>"

# Send as object containing a find object and a replace object to update
@app.route('/api', methods=['PUT'])
def updateRecord():
  myquery = request.json['find']
  newvalues = { "$set": request.json['replace'] }
  collection.update_one(myquery, newvalues)
  return "<p>Record updated.</p>"

# Send as object the criteria to determine which record should be deleted
@app.route('/api', methods=['DELETE'])
def deleteRecord():
    collection.delete_one(request.json)
    return "<p>Record deleted.</p>"

# Start server listening
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)