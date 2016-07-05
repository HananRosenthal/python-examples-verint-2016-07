##################Part 3
import os
import sys
import argparse

parser = argparse.ArgumentParser(description='The program gets a path where file sizes over a pre-defined value are deleted, if required by the user')
parser.add_argument('-p','--path', help='full path (\ - terminated) to search', required=True)
parser.add_argument('-ms','--minsize', help='The size threshold', required=True)
args = vars(parser.parse_args())
#print(args)
'''
if len(sys.argv) != 3:
    print('Usage: %s <path> ,minsize>' % sys.argv[0])
    sys.exit(1)

(_, path, minsize) = sys.argv
'''
#print('Starting at %s, looking for file sizes bigger than %d' % (args['path'], int(args['minsize'])) )

for name in os.listdir(args['path']):
    #print('%s'% name)
    #statinfo = os.stat(path +  name)
    #print(statinfo)
    size = os.path.getsize(args['path'] + name)
    if size > int(args['minsize']):
        #print(size)
        print('Delete %s? [1 for YES 0 for NO]' % (args['path'] + name))
        ans = input()
        if int(ans) == 1:#delete the file
           os.remove(args['path'] + name)