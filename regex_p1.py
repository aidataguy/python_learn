#! /usr/bin/python3

""" My phone number is 412-222-9909 """
import re

areacode = ''
phonenumber = ''

stringdata = "My phone number is 412-222-9909"

phoneregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

patternedPhoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

noPattern = patternedPhoneRegex.search(stringdata)
# no = phoneregex.search(stringdata)

# number = noPattern.group()
areacode = noPattern.group(1)
phonenumber = noPattern.group(2)


print( areacode, phonenumber )


