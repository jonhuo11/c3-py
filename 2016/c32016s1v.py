# verified by DMOJ

import sys

a = input()
b = input()

dc = {}

for c in b:
    if c not in dc:
        dc[c] = 1
    else:
        dc[c] += 1

for c in a:
    # if there is a char left, subtract
    # otherwise check if there are wildcards, if not then fail
    if (c in dc) and dc[c] > 0:
        dc[c] -= 1
    else:
        if "*" in dc and dc["*"] > 0:
            dc["*"] -= 1
        else:
            print("N")
            sys.exit()

print("A")
