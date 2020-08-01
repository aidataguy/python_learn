#! /usr/bin/python3

def caps_decorator(function):
    def caps_wrapper():
        func = function()
        make_caps = func.upper()
        return make_caps
    
    return caps_wrapper


def split_letters(function):
    def split_wrapper():
        func = function()
        split_words = func.split()
        return split_words
    return split_wrapper

def  decortion_with_args(function):
    def wrap_with_args(arg1, arg2):
        print("My cities are: {0}, {1}".format(arg1, arg2))
        function(arg1, arg2)
    return wrap_with_args

