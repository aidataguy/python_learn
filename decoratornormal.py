#! /usr/bin/python3

def mult_two(num):
    return num * 2

    
def func_call(function):
    num_to_mult = 15
    return function(num_to_mult)

print(func_call(mult_two))

def hello_func():
    def say_hello():
        return "Hello"
    return say_hello

hello = hello_func()

print(hello())