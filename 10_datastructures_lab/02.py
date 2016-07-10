################ Part 2
from random import randint

grades = []
for i in range(1, 21):
    grades.append(randint(1,100))

print('The grades are:{}'.format(grades))

avg = float(sum(grades)/len((grades)))
print('The average grade is {}'.format(avg))

for i in grades:
    if i > avg:
        print(grades.index(i))