import csv
import argparse
import string

parser = argparse.ArgumentParser(description='')
parser.add_argument('-p','--path', help='csv file', required = True)
kuku = parser.parse_args()

with open(kuku.path, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 1:
            row[0],row[1] = row[1],row[0]
        print(row)
