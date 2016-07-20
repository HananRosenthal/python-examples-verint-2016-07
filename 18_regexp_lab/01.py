import argparse
import string
import re
'''
parser = argparse.ArgumentParser(description='Returns a parameter that match a given key')
parser.add_argument('-p','--path', help='definitions file', required = True)
parser.add_argument('-k','--key', help='key', required = True)
kuku = parser.parse_args()

with open(kuku.path, 'r') as f:
    for line in f:
        temp = line.split()
        if temp[0].startswith('#'):
            continue
        elif temp[0] == kuku.key:
            res = re.search("=\s+(\w*)", line)
            print(res.group(1))
'''
#After change of attitude :)
with open(kuku.path, 'r') as f:
    for line in f:
        temp = line.split()
        if temp[0].startswith('#'):
            continue
        m = re.search(r'(\w+)\s*=\s*(\w*\s*\w*)', line)
        if m.group(1) == kuku.key and m is not None:
            print(m.group(1), '==>', m.group(2) )

