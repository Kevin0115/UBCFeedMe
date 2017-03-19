import facebook
import requests
import time
import json

accessToken = 'EAACEdEose0cBAJXZBGPbZAfzAUb1js9dqmsHsnJerinKhUIw2fzdSycYPJR7LwqaADJnadMNAON6Tv7fj7g8b4cAsOspteNFhERqPPyYpdYnLqqhwu42zo39zuwqiZCF1hn0dvJTJHdInZB2D37HYifyeNaUNd57ZC7c1NKrjL5SHznLEDmIBtRqD7VZB8KnIZD'
filepath = 'universalAccessCode.txt'
universalAccessCode = "800557763431706%7Cqpv6eBTlNwdkhxd4zyy1NbfxGFs"

# TODO: make the universal code read from file and actually work
# with open(filepath, 'r') as file:
#     universalAccessCode = file.read()

#print(universalAccessCode)
page_ids = ['1035693569787773']
#page_ids = ['bbcnews/events']

events = []
for id in page_ids:
    event = requests.get("https://graph.facebook.com/v2.7/",
                          params={
                              "ids": id,
                              "fields": "events.fields(id,name,start_time,description,place).since({0})".format(time.strftime("%Y-%m-%d")),
                              "access_token": universalAccessCode,
                        }
                        )

    #print(event.json())
    event = event.json()[id]['events']['data']
    events = events + event

print(events)

#"fields": "events.fields(id,name,start_time,description,place,type,category,ticket_uri,cover.fields(id,source),picture.type(large),attending_count,declined_count,maybe_count,noreply_count).since({0}),id,name,cover.fields(id,source),picture.type(large),location".format(
                              #    time.strftime("%Y-%m-%d")),