################### Part 6
from random import randint

r1 = randint(1, 1000)
r2 = randint(1, 1000)

print('%d  %d' % (r1, r2))


mini = min(r1,r2)
maxi = max(r1,r2)
i = int(maxi/mini)

while True:
    if i*mini % maxi == 0:
        break
    i += 1

print('The least common multiple of the two numbers is: {}'.format(i*mini))
