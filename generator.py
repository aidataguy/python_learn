#! /usr/bin/python3
class data(object):
    def __init__(self, n):
        self.n = n
        self.num = 0
    
    def __iter__ (self):
        return iter(self)


    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        else:
            raise StopIteration()


sum_of = sum(data(5000))
            
