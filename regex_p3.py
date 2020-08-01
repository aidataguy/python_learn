#! /usr/bin/python3
import re

supermanRegex = re.compile(r'super(wolf)?man')

data = supermanRegex.search("The adventure of superman")

print(data.group())

data1 = supermanRegex.search("The adventure of superwolfman")

print(data1.group())
supermanRegex = re.compile(r'super(wo)*man')

data = supermanRegex.search("The adventure of superman")

print(data.group())

data1 = supermanRegex.search("The adventure of superwowowoman")

print(data1.group())

supermanRegex = re.compile(r'super(wo)+man')

data = supermanRegex.search("The adventure of superwoman")

print(data.group())

data1 = supermanRegex.search("The adventure of superwowowoman")

print(data1.group())