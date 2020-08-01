#! /usr/bin/python3
import re

superhero = re.compile(r'Superman|Mr Clark ')

data = superhero.search("Superman and Clark are same person")

print(data.group())

data1 = superhero.search(" Mr Clark and Superman  are same person")


print(data1.group())

