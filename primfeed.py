import json
import random
import requests

def json_default(object):
    """workaround for converting objects into json strings"""
    return object.__dict__

def make_post(title, body):
    response = requests.post('http://34.207.10.230:3000/posts', data={"post'_ID": random.randint(1,1000), "title": str(title), "body": body})
    return str(response)

def make_comment(post_ID, title, body):
    response = requests.post('http://34.207.10.230:3000/comments', data={"post'_ID": post_ID, "title": str(title), "body": str(body)})
    return str(response)

def view_posts():
    response = requests.get('http://34.207.10.230:3000/posts')
    print response.text
    return str(response)

################for testing only#############################################
class Post(object):
    def __init__(self, title, body):
        self.post_ID = random.randint(1, 1000)
        self.title = title
        self.body = body


class Comment(object):
    def __init__(self, id, title, body):
        self.post_ID = id
        self.title = title
        self.body = body
