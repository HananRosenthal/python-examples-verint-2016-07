################## Part 4
text = []
while 1:
    print('Please enter a string')
    tmp = input()
    if len(tmp) <= 0:
        break
    text.append(tmp)
    #print(text)

i = len(text)
while i > 0:
    print(text[i-1])
    i -= 1
