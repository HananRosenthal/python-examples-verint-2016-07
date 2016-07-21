import argparse
import string
import re

parser = argparse.ArgumentParser(description='Returns a parameter that match a given key')
parser.add_argument('-p','--path', help='definitions file', required = True)
parser.add_argument('-k','--key', help='key', required = True)
kuku = parser.parse_args()

with open(kuku.path, 'r') as f:
    for line in f:
        prefix = re.match(r'\s*#', line)
        if prefix:
            continue
        m = re.search(r'(\w+)\s*=\s*(.*)', line)
        if m and m.group(1) == kuku.key:
            mm=m.group(2).strip() #remove whitespaces at the end of whatever string is
            print(m.group(1), '==>', mm )
