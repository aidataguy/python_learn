#! /usr/bin/python3

"""
Advantages of Recursion

    Recursive functions make the code look clean and elegant.
    A complex task can be broken down into simpler sub-problems using recursion.
    Sequence generation is easier with recursion than using some nested iteration.

Disadvantages of Recursion

    Sometimes the logic behind recursion is hard to follow through.
    Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
    Recursive functions are hard to debug.
"""

def factorialnum(x):

    if x == 1:
        return 1
    else:
        return (x * factorialnum(x-1))


# number = 5

# print("Factorial is ", factorialnum(number))

def recursion():
    recursion()
recursion()