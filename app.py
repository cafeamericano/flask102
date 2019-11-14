from flask import Flask, request, jsonify
import pymongo
import os
import json

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["flask102"]
mycoll = mydb["wines"]

@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Hello World</h1><p>Sent to you by a server running Flask.</p>"

@app.route('/findone', methods=['GET'])
def test_json():
    query = { "boldness": "heavy" }
    data 
    print(data)
    return json.dumps(data, default=str)

@app.route('/findmany', methods=['GET'])
def test_json2():
    data = mycoll.find().sort('name')
    print(data)
    arr = []
    for item in data:
      arr.append(item)
    return json.dumps(arr, default=str)

@app.route('/insert', methods=['GET'])
def addRecord():
    mydict = { "name": "Zinfandel", "boldness": "medium" }
    x = mycoll.insert_one(mydict)
    return "<p>Record added.</p>"

@app.route('/delete', methods=['GET'])
def deleteRecord():
    myquery = { "name": "Malbec" }
    mycoll.delete_one(myquery)
    return "<p>Record deleted.</p>"

@app.route('/update', methods=['GET'])
def updateRecord():
  myquery = { "name": "Cabernet Sauvignon" }
  newvalues = { "$set": { "name": "Cabernet" } }
  mycoll.update_one(myquery, newvalues)
  return "<p>Record updated.</p>"

@app.route('/query', methods=['GET'])
def test_json3():
    myquery = { "boldness": "heavy" }
    data = mycoll.find(myquery)
    print(data)
    arr = []
    for item in data:
      arr.append(item)
    return json.dumps(arr, default=str)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)