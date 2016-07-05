####################### Part 5
while 1:
    r = randint(1, 1000000)
    if (r % 7 == 0) and (r % 13 == 0) and (r % 15 == 0):
        print('{}'.format(r))
        break

