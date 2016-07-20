import re

def toCamelClass(value):
    output = ""
    Overfirstword = False
    for word in value.split("_"):
        if not word:
            output += ""
            continue
        if Overfirstword:
            output += word.capitalize()
        else:
            output += word.lower()
            Overfirstword = True
    return output

def fromCamelCase(value):
    return re.sub('([A-Z]+)', r'_\1', value).lower()


test = '__hanan_rosenthal_The_second'
res = toCamelClass(test)
print( res)
back = fromCamelCase(res)
print(back)
