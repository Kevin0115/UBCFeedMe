import pymongo
import pprint

from pymongo import MongoClient

# author: Kevin
# sample code that demonstrates how to update/create/delete documents in a specific collection on MongoDB

#### SETUP THE CLIENT ####

# initialize the MongoClient
client = MongoClient()
client = MongoClient('mongodb://Kevin0115:K3vinCh0i!@ds135800.mlab.com:35800/ubcfeedme')
# get an instance of the database
db = client['ubcfeedme']
# get the collection
collection = db.testpy

# JUST FOR TESTING: FLUSH THE COLLECTION
result = db.testpy.delete_many({})