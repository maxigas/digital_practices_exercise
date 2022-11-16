#!/bin/bash

# Dependencies:
# apt install wbritish-huge

# Grab about 1000 (993 in my installation) words from the huge British dictionary list
sed -n '0~p350' /usr/share/dict/british-english-huge > words.txt

# Source and explanation:
# https://unix.stackexchange.com/questions/369181/printing-every-nth-line-out-of-a-large-file-into-a-new-file

