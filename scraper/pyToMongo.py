import pymongo
import pprint

from pymongo import MongoClient

# author: Kevin
# sample code that demonstrates how to update/create/delete documents in a specific collection on MongoDB

# initialize the MongoClient
client = MongoClient()
client = MongoClient('mongodb://Kevin0115:K3vinCh0i!@ds135800.mlab.com:35800/ubcfeedme')

# get an instance of the database
db = client['ubcfeedme']
# get the collection
collection = db['testpy']

# a sample document for test entry
sampleDoc = {"_id": "123456", 
			"event": "Pi Day", 
			"organization": "UBC Engineering", 
			"date": "2017-03-14", 
			"start_time": "08:00:00", 
			"end_time": "20:00:00",
			"location": "Kaiser Atrium",
			"url": "http://facebook.com/freefood"}

sampleDoc2 = {"_id": "246810", 
			"event": "July 4th", 
			"organization": "Murricuh", 
			"date": "2017-07-04", 
			"start_time": "08:00:00", 
			"end_time": "20:00:00",
			"location": "MURRICUH",
			"url": "http://facebook.com/MURRICUH"}

# holds the postings for the collection
allPosts = db.testpy

# JUST FOR TESTING: FLUSH THE COLLECTION
result = db.testpy.delete_many({})

# inserts a document to the collection
result = allPosts.insert_one(sampleDoc2)
result.inserted_id
result = allPosts.insert_one(sampleDoc)
result.inserted_id
db.collection_names(include_system_collections=False)
[u'testpy']

# check if a document exists in the collection (just prints)
print(allPosts.find_one({"_id": "123456"}) == None)

# check pymongo documentation for any other queries