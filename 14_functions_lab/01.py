from functools import reduce

#function tha returns the sum of input parameters
def mysum(*nums):
    return sum([n for n in nums if type(n) == int])

#function tha returns the product of input parameters
def mymul(*nums):
    list=[]
    for number in nums:
        if type(number) is int:
            list.append(number)

    return  reduce(lambda x, y: x*y, list)

print('Sum= ', mysum('r', 1,2,'a','b'))
print('Mul= ', mymul('t', 1,2,3,4,'s') )

