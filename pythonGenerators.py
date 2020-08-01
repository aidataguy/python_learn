#! /usr/bin/python3

class MyData(object):
    def __init__(self, n, nums ):
        self.n = n
        self.nums = 0

    def __iter__(self):
        return myFinalData(self.n, self.nums)


class myFinalData(object):
    def __init__(self, n, nums):
        self.current = n
        self.nums = nums

    
    def __next__(self):
        if self.nums >= self.current:
            raise StopIteration
        to_return = self.nums
        self.nums += 1

        return to_return

my_valuable_data = MyData(1000000, 10)

x = sum(my_valuable_data)

print(x)
