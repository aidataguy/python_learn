#! /usr/bin/python3

# lambda arguments: expression

cube = lambda x: x * 3

print(cube(9))

# filtering using lambda

my_list = [10, 21, 44, 54, 72, 22, 30, 50]

new_list = list(filter(lambda x: (x%2 == 0 ), my_list))

print(new_list)

# map using lambda

list_map = [10, 21, 44, 54, 72, 22, 30, 50]

mapped_list =  list(map(lambda x:x * 2, list_map))

print(mapped_list)