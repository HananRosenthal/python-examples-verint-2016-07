import collections
import string

f = lambda s: s[0]

def groupby(f, *words):
    myDict = {}
    for word in words:
        k = f(word)
        list = [w for w in words if w[0] == k]
        myDict[k] = list
    print(myDict)

words = ["hello", "hi", "help", "bye", "here", "modify", "movie", "typo", "time"]
groupby(f, *words)
