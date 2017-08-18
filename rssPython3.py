from urllib.request import Request, urlopen
from urllib.error import URLError
import json

api_url = Request('http://34.207.10.230:3000/posts')

try:
    response = urlopen(api_url)
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    else:
        # everything is fine
        values = {'sender': 'Peter', 
                'receiver': 'Team 2',
                'message': 'WE CRACK THIS EVERYDAY'}
        headers = {'Content-type': 'application/json',
                'Accept': 'text/plain'}

        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
        req = urllib.request.Request(api_url, data, headers)
        with urllib.request.urlopen(req) as response:
        the_page = response.read()
