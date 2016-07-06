################# Part 7

while True:
    r1 = randint(1, 10) # a random number
    #print('{}'.format(r1))
    guess = int(input('Please gusee a number in the range 1 - 100')) #The user guess
    if guess == r1:
        print('BINGO')
        break
    if guess < r1:
        print('your guess ({}) is too small'.format(guess))
    else:
        print('your guess ({}) is too big'.format(guess))
