#! /usr/bin/python3
from createdec import caps_decorator, split_letters, decortion_with_args

@split_letters
@caps_decorator

def say_hello():
    return 'hello himanshu'



@decortion_with_args
def myCities(city1, city2):
    print(" Cities I love are {0} and {1}".format(city1, city2))

myCities("Yekaterinburg", "Krasnoyarsk")

# print(say_hello())