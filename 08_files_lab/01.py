import argparse

parser = argparse.ArgumentParser(description='The program gets two files and adds the content of the first one to the end of the second file')
parser.add_argument('-f1','--file1', help='file1 full path', required = True)
parser.add_argument('-f2','--file2', help='file2 full path', required = True)
kuku = parser.parse_args()

with open(kuku.file1, 'r') as fin:
    with open(kuku.file2, 'a') as fout:
        for line in fin:
            fout.write(line)
