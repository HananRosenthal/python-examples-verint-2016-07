############### Part 2
sum=0
L = 7
for i in range(0,L):
    r = randint(1,100)
    sum += r
    print('%d' % r)

print('The sum of the seven random numbers is {}'.format(sum))
if sum % L == 0:
    print('%s' % 'Boom')
#How many times (on the average) should we run this program in order to get a 'Boom'?
