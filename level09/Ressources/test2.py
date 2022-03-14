#!/usr/bin/python

# execute like this : python /tmp/test2.py $(cat token)

import sys

def reverse_string(string):
    ret_string = ""
    for i, char in enumerate(string):
        ret_string += chr((ord(char) - i))
    return ret_string

s = sys.argv[1]
print(reverse_string(s))
