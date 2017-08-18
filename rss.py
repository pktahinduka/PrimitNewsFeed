import json
import urllib.request
import requests
import urllib.parse

api_url = "http://34.207.10.230:3000/posts"

# API below returns an array of complex JSON objects
jsonobj = json.load(urllib.request.urlopen(api_url))

# index into the array and access a sub-attribute like this:
print(jsonobj[5])

values = {'sender': 'Peter', 'receiver': 'Team 2', 'message': 'WE CRACK THIS EVERYDAY'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(api_url, data=json.dumps(values), headers=headers)

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(api_url, data, headers)
with urllib.request.urlopen(req) as response:
   the_page = response.read()
