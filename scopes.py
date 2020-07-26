#! /usr/bin/python3

def result(divideBy):
    return 800 / divideBy

try:
    print(result(20))
    print(result(35))
    print(result(0))
except ZeroDivisionError:
    print("Error: You cannot divide it by zero")
