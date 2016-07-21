import csv
import argparse
import string
import re

parser = argparse.ArgumentParser(description='')
parser.add_argument('-p','--path', help='csv file', required = True)
kuku = parser.parse_args()

with open(kuku.path, 'r') as f:
    reader = csv.reader(f)
    num_cols = len(next(reader))
    f.seek(0 ,0)

    for row in reader:
        if num_cols > 1:
            row[0],row[1] = row[1],row[0]
            print(row)
        else:#print as is...
            print(row)
