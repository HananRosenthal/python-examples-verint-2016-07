##################Part 1
import os
import sys

if len(sys.argv) != 2:
    print('Usage: %s <number of repetions>' % sys.argv[0])
    sys.exit(1)

(_, num) = sys.argv
print('number of repetitions = {}'.format(num) )
#print('{}'.format(type(num)))

for i in range (0, int(num)):
    print('Hello Python')

