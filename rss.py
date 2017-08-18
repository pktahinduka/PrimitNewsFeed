import json
import urllib2
import requests

api_url = "http://34.207.10.230:3000/posts"

# API below returns an array of complex JSON objects
jsonobj = json.load(urllib2.urlopen(api_url))

# index into the array and access a sub-attribute like this:
print jsonobj[5]

data = {'sender': 'Peter', 'receiver': 'Team 2', 'message': 'WE CRACK THIS EVERYDAY'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(api_url, data=json.dumps(data), headers=headers)

def getPost()