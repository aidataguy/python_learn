#! /usr/bin/python3

from classInheritance import  HousePrototype as hp

""" This has all classinheritance classes imported  """
# import classInheritance


new_house = hp('Red', 8, 'Volgagrad')

print(new_house.paint())
print(new_house.build_floor())

# new_villa = classInheritance.House('Purple', 2, "Stalingrad")

# print(new_villa.location.get_location())