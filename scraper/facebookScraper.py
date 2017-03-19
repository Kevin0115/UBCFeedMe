import facebook
import requests
import time
import json
import re

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
    #print(event)
    organizer = organizer.json()['name']
    for e in event:
        e['organization'] = organizer
    events = events + event

print(events)

# filters events. If a bad word is found the event is either not free or doesn't have food. Skip it.
# If a bad word is not found and a good word is (ie. the event likely has free food), add is to the list
valid_events = []
for event in events:
    try:
        description = event['description'].lower()
    except Exception:
        continue

    for word in badWords:
        if description.find(word):
            print("removing a thing")
            break
    else:
        for goodWord in goodWords:
            if description.find(goodWord):
                # event has free good. add to list
                valid_events.append(event)
                break

# format the event fields
for event in valid_events:
    event['date'] = event['start_time'].split('T')[0]
    event['start_time'] = event['start_time'].split('T')[1]
    event['end_time'] = event['end_time'].split('T')[1]
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



    #print('{}, {}, {}'.format(event['date'], event['start_time'][:-5], event['end_time'][:-5]))
    #print(event)
print("valid events")
print(valid_events)