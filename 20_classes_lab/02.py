##### Exercise-2 ##################
class MyCounter(object):
    counter = []

    def __init__(self):
        self.counter.append(1)

    @classmethod
    def count(self):
        return sum(MyCounter.counter)


for _ in range(10):
    c1 = MyCounter()

# should print 10
print(MyCounter.count())
