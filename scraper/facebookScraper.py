import facebook
import requests
import time
import json

filepath = 'universalAccessCode.txt'
universalAccessCode = "800557763431706%7Cqpv6eBTlNwdkhxd4zyy1NbfxGFs"

# TODO: make the universal code read from file and actually work
# with open(filepath, 'r') as file:
#     universalAccessCode = file.read()

#print(universalAccessCode)
page_ids = ['UBCEngineers', 'susubc']

events = []
for id in page_ids:
    event = requests.get("https://graph.facebook.com/v2.8/",
                          params={
                              "limit": 100,
                              "ids": id,
                              "since": time.strftime("%Y-%m-%d"),
                              "fields": "events.fields(id,name,start_time,end_time,description,place)",
                              "access_token": universalAccessCode,
                        }
                        )

    event = event.json()[id]['events']['data']
    events = events + event

print(events)