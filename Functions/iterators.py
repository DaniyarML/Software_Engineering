# need __iter__ and __next__ methods
# need to track internal state
# need to raise exception in the end

class MyIter:
    def __init__(self, size=0):
        self.max = size
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 2**self.n
            self.n += 1
            return result
        else:
            raise StopIteration

for i in MyIter(5):
    print(i)