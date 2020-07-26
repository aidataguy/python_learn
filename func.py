#! /usr/bin/python3
'''
This program will tell you
how to write a function.
'''

def hello(name):
    if len(name) < 5 :
        return "hey your name is too short " + name
    elif len(name) >= 5:
        return "You have a perfect name" + name

myName = hello("Trenton")
print(myName)


