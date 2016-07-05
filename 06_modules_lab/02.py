#####################Part 2
import os
import sys

if len(sys.argv) != 3:
    print('Usage: %s <num1>  <num2> ' % sys.argv[0])
    sys.exit(1)

(_, num1, num2) = sys.argv

num1 = int(num1)
num2 = int(num2)

print('%d %d %d' % (num1, num2, num1+num2))


