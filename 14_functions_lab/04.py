
def get_words(max_len, *words):
    list=[]
    for word in words:
        if len(word) > max_len:
            list.append(word)
    return  list

print( get_words(3,'a','aa','vvdd', 'tresd', 'ww') )
