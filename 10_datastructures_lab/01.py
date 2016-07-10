################Part 1
import argparse
#-*- coding: utf-8 -*-
#print(u'\u05ea\u05d0\u05de\u05d9\u05df \u05dc\u05d9')
#print(u'\u05e9\u05dc\u05d5\u05dd')

parser = argparse.ArgumentParser(description='Gets to strings, one for "user-name" and the second for "password".'
                                             'If these have a match in a given table, prints a welcome messge, otherwise prints n0-entrance')
parser.add_argument('-s1','--string1', help='first input string', required = True)
parser.add_argument('-s2','--string2', help='second input string', required = True)
kuku = parser.parse_args()

table = {'apple': 'red', 'lettuce': 'green', 'lemon': 'yellow', 'orange': 'orange'}

if kuku.string1 in table:
    if table[kuku.string1] == kuku.string2:
        print('Welcome')
        print(u'\u05d1\u05e8\u05d5\u05db\u05d9\u05dd \u05d4\u05d1\u05d0\u05d9\u05dd')
    else:
        print('Failed')
        print(u'\u05d0\u05d9\u05df \u05db\u05e0\u05d9\u05e1\u05d4')
