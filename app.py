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

# Routing
@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Hello World</h1><p>Sent to you by a server running Flask.</p>"

@app.route('/findmany', methods=['GET'])
def test_json2():
    data = collection.find().sort('name')
    print(data)
    arr = []
    for item in data:
      arr.append(item)
    return json.dumps(arr, default=str)

@app.route('/insert', methods=['GET'])
def addRecord():
    mydict = { "name": "Zinfandel", "boldness": "medium" }
    x = collection.insert_one(mydict)
    return "<p>Record added.</p>"

@app.route('/delete', methods=['GET'])
def deleteRecord():
    myquery = { "name": "Malbec" }
    collection.delete_one(myquery)
    return "<p>Record deleted.</p>"

@app.route('/update', methods=['GET'])
def updateRecord():
  myquery = { "name": "Cabernet Sauvignon" }
  newvalues = { "$set": { "name": "Cabernet" } }
  collection.update_one(myquery, newvalues)
  return "<p>Record updated.</p>"

@app.route('/query', methods=['GET'])
def test_json3():
    myquery = { "boldness": "heavy" }
    data = collection.find(myquery)
    print(data)
    arr = []
    for item in data:
      arr.append(item)
    return json.dumps(arr, default=str)

# Start server listening
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)