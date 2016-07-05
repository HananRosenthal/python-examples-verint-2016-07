################# Part 7
while 1:
    r1 = randint(1, 10)
    #print('{}'.format(r1))
    print('Please gusee a number in the range 1 - 100')
    r = int(input())
    if r == r1:
        print('BINGO')
        break
    if r < r1:
        print('your guess ({}) is too small'.format(r))
    else:
        print('your guess ({}) is too big'.format(r))

########################### End of Syntax exercise ############################
