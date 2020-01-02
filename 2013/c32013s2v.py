# verified by DMOJ

import sys

w = int(input())
n = int(input())
cars = [int(input()) for x in range(n)]

counter = 0

for i in range(3, len(cars)):
    if cars[i - 3] + cars[i - 2] + cars[i - 1] + cars[i] > w:
        sum = 0
        for j in range(i - 3, i + 1):
            sum += cars[j]
            if sum > w:
                print(counter)
                sys.exit()
            else:
                counter += 1
    else:
        counter += 1

print(len(cars))
