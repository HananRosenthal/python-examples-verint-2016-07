################Part 3
import argparse

parser = argparse.ArgumentParser(description='The program gets a host name from the user and search for it in a table')
parser.add_argument('-p','--path', help='hosts file full path', required = True)
kuku = parser.parse_args()

hosts={} #dictionary declaration

#build the dictionary
with open(kuku.path, 'r') as f:
    for line in f:
        (device, address) = line.split("=")
        hosts[device] = address

#get a string from user and search for a match
while True:
    strr = input('Please enter a device name, enter to exit')
    if strr == "":
        break
    elif strr in hosts:
        print(hosts[strr])
    else:
        print('Device {} not found'.format(strr))

print('Thank you and goodbye')