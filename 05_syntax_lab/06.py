################### Part 6
r1 = randint(1, 10)
r2 = randint(1, 10)
maximum = r1 * r2
print('r1 = %d r2 = %d max quotient = %d' % (r1, r2, maximum))
i = 1
min_quotient = []
while i <= maximum:
    if (i % r1 == 0) and (i % r2 == 0):
        min_quotient.append(i)
        #print('{}'.format(min_quotient))
    i += 1

print('%d' % min(min_quotient))

