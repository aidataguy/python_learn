#! /usr/bin/python3

class HousePrototype:
    def __init__(self, color, floors, location):
        self.color = color
        self.floors = floors
        self.location = location
    
    def paint(self):
        return (f"{self.color} is painted. ")
    
    def build_floor(self):
        return (f"{self.floors} are to be built. ")

    def build_location(self):
        print(f"{self.location} are to be built. ")

    
class HouseLocation:
    def __init__(self, house_location="New Delhi"):
        self.location = house_location
    def get_location(self):
        print(f"The location is {self.location} . ")

# child class
class House(HousePrototype):
    def __init__(self, color, floors, location):
        super().__init__(color, floors, location)
        self.year_of_build = 2018
        self.location = HouseLocation()

    def get_build_year(self):
        print(f"The house was built in {self.year_of_build}. ")
    
    def build_location(self):
        print("You cannot allocate the location to the same house")


# my_new_house = House("blue", 4, "Pochinki")
# my_new_house.location.get_location()

