import pymongo
import pprint
import datetime

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


#-----------------------------FLUSH (we re-scrape anyways)


#-----------------------------ACQUIRE DATA

# COMPLETED BY MATHEW AND ALEX


#-----------------------------FILTER AND FORMAT

# COMPLETED BY MATHEW

#-----------------------------PUSH DATA TO DATABSE

# COMPLETED BY KEVIN
pushData(events)


# for each new arrival of events, check against the database for duplicates
# don't use this; maybe for error checking JUST in case
def checkDuplicates(event):
    if collection.find_one({"_id": it_event["_id"]}):
        return true
    else:
        return false


# deletes all documents in the collection
def deleteAll():
    result = db.testpy.delete_many({})

def pushData():
    for it_event in events:
        if checkDuplicates:
            


# -------------------------------- FOR TESTING
events = [{"_id": "123456", 
            "event": "Pi Day", 
            "organization": "UBC Engineering", 
            "date": "2017-03-14", 
            "start_time": "08:00:00", 
            "end_time": "20:00:00",
            "location": "Kaiser Atrium",
            "url": "http://facebook.com/freefood"},
            {"_id": "246810", 
            "event": "July 4th", 
            "organization": "Murricuh", 
            "date": "2017-07-04", 
            "start_time": "08:00:00", 
            "end_time": "20:00:00",
            "location": "MURRICUH",
            "url": "http://facebook.com/MURRICUH"}]


deleteAll()

# inserts a document to the collection
result = collection.insert_one(events[0])
result.inserted_id
db.collection_names(include_system_collections=False)
[u'testpy']

# check if a document exists in the collection (just prints)

# check pymongo documentation for any other queries

# -------------------------------- DONE TESTING