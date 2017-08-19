"""
Usage:
primfeed view_feed
primfeed post <title> <body>
primfeed comment <postId> <title> <body>
options:
quit to exit the application
"""

import cmd
import requests
import json
import os
from docopt import DocoptExit, docopt



def intro():
    print(__doc__)


def docopt_cmd(func):

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as err:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(err)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class PrimitiveNewsFeed(cmd.Cmd):
    os.system("cls")
    prompt = "primfeed "


    def __init__(self):
        self.apiURL = "http://34.207.10.230:3000/"
        super().__init__()

    @docopt_cmd
    def do_view_feed(self, args):
        """Usage: view_feed"""
        # consider showing the post title and post body for each post there is.
        feed_url = self.apiURL + "posts"
        resp = requests.get(feed_url)
        print(resp.json())
        print()

    @docopt_cmd
    def do_post(self, args):
        """Usage: post <title> <body>"""

        body = args['<body>']
        title = args['<title>']

        data = dict(title=title, body=body)
        headers = {"Content-Type": "application/json", "Accept": "text/plain"}
        post_url = self.apiURL + "posts"
        resp = requests.post(post_url, data=json.dumps(data), headers=headers)
        if int(resp.status_code) == 201:
            print("Your data has been posted")
        else:
            print("You have an error somewhere")
        print()

    @docopt_cmd
    def do_comment(self, args):
        """Usage: comment <postId> <title> <body>"""
        postId = args["<postId>"]
        title = args["<title>"]
        body = args["<body>"]

        data = dict(postId=postId, title=title, body=body)
        headers = {"Content-Type": "application/json", "Accept": "text/plain"}

        comment_url = self.apiURL + "comments"
        r = requests.post(comment_url, data=json.dumps(data), headers=headers)
        if int(r.status_code) == 201:
            print("Your comment has been registered /posted")
        else:
            print("We are having trouble posting your comment")
        print()

    def do_quit(self, args):
        """Usage: quit"""
        os.system('cls')
        print('Application Exiting')
        exit()

PrimitiveNewsFeed().cmdloop()