#! /usr/bin/python3
#while with break continue!!

while True:
    print("Please type your name")
    name = input()
    if name == "your name":
        break
    else:
        continue
print("Hey your name is" + name)
