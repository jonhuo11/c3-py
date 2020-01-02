# this problem is an optimization problem
# on DMOJ this solution goes over the time limits


import sys

# num of gate
g = int(input())
# num of plane
p = int(input())

planes = [int(input()) - 1 for x in range(p)]
gates = [False for x in range(g)]

amt = 0
for plane in planes:
    past = False
    for gt in reversed(range(plane + 1)):
        if gates[gt] == False:
            gates[gt] = True
            amt += 1
            past = True
            break
    if past == False:
        print(amt)
        sys.exit()

print(amt)
