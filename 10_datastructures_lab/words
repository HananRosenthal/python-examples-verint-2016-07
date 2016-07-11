################Part 4
import argparse

parser = argparse.ArgumentParser(description='look for anagrams in the input file')
parser.add_argument('-p','--path', help='', required = True)
kuku = parser.parse_args()

li=[]
freq={}
word_dic={}
keys = []

#Populate a list with all words in the input file (each word contains the \n at its end)
with open(kuku.path, 'r') as f:
    for line in f:
        li.append(line)

#Create a word dictionary, with letter distribution for each word
for word in li:
    for letter in word:
        count = freq.setdefault(letter,0)
        freq[letter] = count + 1
    word_dic[word] = freq.copy()
    freq.clear()

#Look fir anagrams
while len(word_dic) > 1:
    iam = word_dic.popitem()
    for key, val in word_dic.items():
        if key != iam[0] and val == iam[1]:
            keys.append(key)

    #Erase anagramatic key's
    length = len(keys)
    if length > 0:
        print('The following words are anagrams\n\r')
        print('{}'.format(iam[0]))
        for i in range(0,length):
            print('{}'.format(keys[i]))

    for i in keys:
        del word_dic[i]
    keys.clear()
