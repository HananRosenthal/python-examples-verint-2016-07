import collections
import string

f = lambda c, wList: [w for w in wList if w[0] == c]

def groupby(f, *words):
    myDict = {}
    list=[]
    for c in string.ascii_letters:
        list = f(c, words)
        if len(list) > 0:
            myDict[c] = list
    print(myDict)

words = ["hello", "hi", "help", "bye", "here", "modify", "movie", "ticho", "time"]
groupby(f, *words)
