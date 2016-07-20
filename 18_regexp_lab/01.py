import argparse
import string
import re

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
