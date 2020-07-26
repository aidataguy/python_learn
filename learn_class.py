#! /usr/bin/python3

class HousePrototype:
    def __init__(self, color, floors, location):
        self.color = color
        self.floors = floors
        self.location = location
    
    def paint(self):
        print(f"{self.color} is painted. ")
    
    def build_floor(self):
        print(f"{self.floors} are to be built. ")

    def build_location(self):
        print(f"{self.location} are to be built. ")


class House(HousePrototype):
    def __init__(self, color, floors, location):
        super().__init__(color, floors, location)


my_new_house = House("blue", 4, "Pochinki")


# my_house = HousePrototype("Blue", 7, "Rozhok")
# your_house = HousePrototype("Red", 4, "Black waters")

print(f"my house's color is {my_new_house.color}. ")
print(f"my house's has {my_new_house.floors} floors. ")
print(f"my house is located at {my_new_house.location} . ")

# print(f"your house's color is {your_house.color}. ")
# print(f"your house has {your_house.floors} floors. ")
# print(f"your house is located at {your_house.location} . ")


# print("#Method tests are:  ")
# my_house.paint()
# my_house.build_floor()