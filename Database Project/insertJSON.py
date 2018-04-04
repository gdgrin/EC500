import sys, urllib2, json, pymongo
from pymongo import MongoClient
from bson import json_util

'''
myurl = "https://gist.githubusercontent.com/tdreyno/4278655/raw/7b0762c09b519f40397e4c3e100b097d861f5588/airports.json"
response = urllib2.urlopen(myurl)
data = json.loads(response.read())
connection = MongoClient('mongodb://localhost')
connection.database_names()
db = connection.database
posts = db.posts
post_id = posts.insert_many(data).inserted_ids
'''

connection = MongoClient('mongodb://localhost')
db = connection.airport
airports1 = db.airport_collection
page = open("airports.json", 'r')
parsed = json.loads(page.read())

for item in parsed["Airports"]:
    airports1.insert(item)