#!/usr/bin/python3
# Dependencies:
# sudo apt install python3-flask ibritish-large
# ./generate-word-list.sh

import flask, random

dictionary = 'words.txt'

def rpl(old, new, filename):
    """Replicate the functionality of the `rpl` command/package in Debian bookworm"""
    with open(filename, 'r') as f:
        data = f.read()
    with open(filename, 'w') as f:
        f.write(data.replace(old, new))

def word():
    """Choose random word, scratch it off the list, return the choice"""
    words = [line.strip() for line in open(dictionary, 'r') if '!' not in line]
    choice = words[random.randint(0,len(words))]
    rpl(choice, '!' + choice, dictionary)
    return choice

app = flask.Flask(__name__)

@app.route("/")
def index():
    return f"<h1>Congratulations!</h1><p>You found the website for the Digital Practices Data Security exercise!</p><p>Your special word is \"{word()}\".</p><p>Please fill in the word to field 1.b on the Answer Form for Assignment 6 on Data Ethics.</p><p>Have a nice day,</p><p><i>Your teachers Lonneke & Maxigas</i></p>"

