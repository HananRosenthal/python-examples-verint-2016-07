################### Part 3
from random import randint

L = 10000
r = randint(1, L)
str_r = str(r)
print('The string number is {}'.format(str_r) )
num_digits = len(str_r)
print('The number %d contains %d digits' % (r,num_digits) )
sum = 0
for c in str_r:
#for i in range(0, num_digits):
    sum += int(c)

print('The sum of digits {}'.format(sum) )
