
f = lambda s: s[0]

def groupby(f, *words):
    myDict = {}
    for word in words:
        k = f(word)
        myDict.setdefault(k, []).append(word)
    print(myDict)

words = ["hello", "hi", "help", "bye", "here", "modify", "movie", "typo", "time", 'jump', 'jumbo', 'murder', 'jamboree']
groupby(f, *words)
