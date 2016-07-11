
alphabet = [chr(x) for x in range(97,123)]
duo = [x+y for x in alphabet for y in alphabet]
res = [x+y for x in alphabet for y in duo]
print(res)