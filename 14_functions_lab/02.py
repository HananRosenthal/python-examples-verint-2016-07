
def get_params(times=3, text=None):
    if type(text) is not str: raise Exception("Type of text")
    if type(times) is not int: raise Exception("Type of times")

get_params(125, 2)