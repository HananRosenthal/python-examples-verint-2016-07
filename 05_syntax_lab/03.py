################### Part 3
L = 10000
r = randint(1, L)
str_r = str(r)
print('The string number is {}'.format(str_r) )
num_digits = len(str_r)
print('The number %d contains %d digits' % (r,num_digits) )
sum = 0
for i in range(0, num_digits):
    sum += int(str_r[i])

print('The digits sum is {}'.format(sum) )
