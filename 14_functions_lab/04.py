def get_words(max_len, *words):
    return [word for word in words if len(word) > max_len]

	
print( get_words(4,'a','aa','vvdd', 'tresd', 'ww') )
