##### Slass Synatx ##################
##### Exercise-1 ##################

class Summer(object):

    def __init__(self):
        self.val = 0

    def add(self, *num):
        self.val += sum([i for i in num])

    def total(self):
        return self.val



s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
print(s.total())

# should print 50
print(t.total())
