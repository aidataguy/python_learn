#!/usr/bin/python3

#set a secret number
# import random
# random.randint(1, 10)
sec_num = 8
print("I am thinking of a number")


#ask for user input
for chances in range(1, 6):
    print("take a guess? ")
    #if not right answer ask for input again
    guess = int(input())
    #check user input
    if guess < sec_num:
        print("Guess num is toooo small")
    elif guess > sec_num:
        print("Guess num is too big")
    else:
        break
if guess == sec_num:
    #if right answer say congrats....
    print("Congrats you guessed it!!")
else:
    print("No the number was " + str(sec_num))




