'''
import math

n = int(input())
woods = sorted([int(x) for x in input().split()])

index = {}
for i in range(0, len(woods)):
    for j in range(0, len(woods)):
        if j == i:
            continue
        try:
            index[str(woods[i] + woods[j])] += 1
        except KeyError as e:
            index[str(woods[i] + woods[j])] = 0
            index[str(woods[i] + woods[j])] += 1

highest = 0
for w in index:
    if index[w] > highest:
        highest = index[w]

amt = 0
for x in index:
    if index[x] == highest:
        amt += 1

print ("%s %s" % (highest/2, amt))
'''
