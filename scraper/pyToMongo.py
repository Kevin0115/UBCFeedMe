from pymongo import MongoClient
import requests
import time
import re

# author: Kevin, Mathew
# sample code that demonstrates how to update/create/delete documents in a specific collection on MongoDB

#### SETUP THE CLIENT ####

# initialize the MongoClient
client = MongoClient()
client = MongoClient('mongodb://Kevin0115:K3vinCh0i!@ds135800.mlab.com:35800/ubcfeedme')
db = client['ubcfeedme'] # get an instance of the database
collection = db.testpy # get the collection

result = db.testpy.delete_many({})

#-----------------------------FLUSH (we re-scrape anyways)


#-----------------------------ACQUIRE DATA

# COMPLETED BY MATHEW AND ALEX
accessCodeFilepath = 'universalAccessCode.txt'
goodWordsFilepath = 'goodWords.txt'
badWordsFilepath = 'badWords.txt'
pageNamesFilepath = 'page_names.txt'
universalAccessCode = "800557763431706%7Cqpv6eBTlNwdkhxd4zyy1NbfxGFs"

# TODO: make the universal code read from file and actually work
# with open(filepath, 'r') as file:
#     universalAccessCode = file.read()

with open(goodWordsFilepath, 'r') as file:
    goodWords = file.read().splitlines()

with open(badWordsFilepath, 'r') as file:
    badWords = file.read().splitlines()

with open(pageNamesFilepath, 'r') as file:
    page_names = file.read().splitlines()


events = []
for name in page_names:
    url = "https://graph.facebook.com/v2.8/{}/events?access_token={}&limit={}&fields=id,name,start_time,end_time,description,place&since={}"\
            .format(name, universalAccessCode, 100, time.strftime("%Y-%m-%d"))
    url2 = "https://graph.facebook.com/v2.8/{}?access_token={}"\
            .format(name, universalAccessCode)

    event = requests.get(url)
    organizer = requests.get(url2)
    try:
        event = event.json()['data']
    except Exception:
        continue

    organizer = organizer.json()['name']
    for e in event:
        e['organization'] = organizer
    events = events + event


# filters events. If a bad word is found the event is either not free or doesn't have food. Skip it.
# If a bad word is not found and a good word is (ie. the event likely has free food), add is to the list
valid_events = []
for event in events:
    try:
        description = event['description'].lower()
    except Exception:
        continue

    bad = False
    for word in badWords:
        if word.lower() in description:
            bad = True
            break

    if int(event['end_time'].split('T')[0].split('-')[2]) - int(event['start_time'].split('T')[0].split('-')[2]) > 2:
        bad = True

    if bad is True:
        continue

    nineteen_plus = False
    regexp1 = re.compile(r'19\+')
    regexp2 = re.compile(r'19 and up')
    regexp3 = re.compile(r'19 plus')

    if regexp1.search(description) or regexp2.search(description) or regexp3.search(description):
        event['name'] = "{}    {}".format(event['name'], "(19+)")

    for goodWord in goodWords:
        if goodWord.lower() in description:
            # event has free good. add to list
            valid_events.append(event)
            break

# format the event fields
for event in valid_events:
    event['date'] = event['start_time'].split('T')[0]
    event['start_time'] = event['start_time'].split('T')[1][:-5]
    event['end_time'] = event['end_time'].split('T')[1][:-5]
    event['_id'] = event['id']
    del event['id']
    event['event'] = event['name']
    del event['name']
    try:
        event['location'] = event['place']['name']
        del event['place']
    except Exception:
        event['location'] = "TBD"
    try:
        del event['description']
    except Exception:
        continue
    event['url'] = "https://www.facebook.com/events/{}".format(event['_id'])

print(len(valid_events))

#-----------------------------PUSH DATA TO DATABSE

# COMPLETED BY KEVIN

def pushData():
    for it_event in valid_events:
        try:
            result = collection.insert_one(it_event)
        except Exception:
            continue
        #result.inserted_id


pushData()
# check if a document exists in the collection (just prints)

# check pymongo documentation for any other queries
