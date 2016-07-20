import argparse
import string
import re

#Finally:
with open(kuku.path, 'r') as f:
    for line in f:
        prefix = re.match(r'\s*#', line)
        if prefix is not None:
            continue
        m = re.search(r'(\w+)\s*=\s*(.*)', line)
        if m.group(1) == kuku.key and m is not None:
            print(m.group(1), '==>', m.group(2) )
