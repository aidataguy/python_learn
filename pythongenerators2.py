#! /usr/bin/python3

# def generator_iter():
#     yield 'xyz'
#     yield 200
#     yield 20.10

# for i in generator_iter():
#     print(i)

# QUick number program

# sq = 200000
# num_list = range(1, sq+1)
# for i in num_list:
#     print(i*i)

def sq_generator(sq):
    num=1
    while True:
        yield num
        if num == sq:
            return
        else:
            num += 1

for i in sq_generator(2580):
    print(i*i)