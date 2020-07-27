#! /usr/bin/python3

filename = "data.txt"

guess_text = ''

with open(filename) as f_obj:
    lines = f_obj.readlines()
    for line in lines:
        guess_text += line.strip()

city = input("Enter city name you want to find ")

if city in guess_text:
    print("Your city is in the text ")
else:
    print("No your city is not in the text")
        
