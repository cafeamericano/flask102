from flask import Flask
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["flask102"]
mycoll = mydb["wines"]

### Find one
x = mycoll.find_one()
print x

### Find all and sort
for record in mycoll.find().sort("name"):
  print(record)

### Query
myquery = { "boldness": "heavy" }
mydoc = mycoll.find(myquery)
for x in mydoc:
  print(x)

### Insert
mydict = { "name": "Cabernet", "boldness": "heavy" }
x = mycoll.insert_one(mydict)

### Delete
myquery = { "name": "Syrah" }
mycoll.delete_one(myquery)

### Update One
myquery = { "name": "Cabernet" }
newvalues = { "$set": { "name": "Cabernet Sauvignon" } }
mycoll.update_one(myquery, newvalues)