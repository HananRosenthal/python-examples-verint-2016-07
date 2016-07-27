##### Exercise-2 ##################
class MyCounter(object):
    counter = 0

    def __init__(self):
        MyCounter.counter += 1
        #print(MyCounter.counter)

    def count(self):
        return MyCounter.counter

for _ in range(10):
    c1 = MyCounter()

# should print 10
print(MyCounter.count(object))
