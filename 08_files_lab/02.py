#############Part 2
import argparse
from itertools import zip_longest

parser = argparse.ArgumentParser(description='The program gets two files and writes their content (line by line) to the 3rd file')
parser.add_argument('-f1','--file1', help='file1 full path', required = True)
parser.add_argument('-f2','--file2', help='file2 full path', required = True)
parser.add_argument('-f3','--file3', help='file3 full path', required = True)
kuku = parser.parse_args()

fin1 = open(kuku.file1, 'r')
fin2 = open(kuku.file2, 'r')
listtt = zip_longest(fin1, fin2, fillvalue="")

fout = open(kuku.file3, 'w')
for item in listtt:
    fout.write(str(item[0]))
    fout.write(str(item[1]))

fin1.close()
fin2.close()
fout.close()