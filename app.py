#!/usr/bin/python3
# Dependencies:
# apt install python3-flask ibritish-large

import flask, random

app = flask.Flask(__name__)

dict_path = "/usr/share/dict/british-english-huge"
words = [line.strip() for line in open(dict_path, 'r')]

@app.route("/")
def index():
    return f"<h1>Congratulations!</h1><p>You found the website for the Digital Practices Data Security exercise!</p><p>Your IP address is {flask.request.remote_addr} and your special word is \"{random.choice(words)} {random.randint(0,1000)}\".</p><p>Please submit these to the 'hidden service' Canvas exercise.</p><p>Have a a nice day,</p><p><i>Your teachers Lonneke & Maxigas</i></p>"

