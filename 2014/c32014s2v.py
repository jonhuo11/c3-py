# verified by DMOJ

import sys

# assigning partners
n = int(input())
ln1 = input().split()
ln2 = input().split()

dc = {}

for i in range(len(ln1)):
    a = ln1[i]
    b = ln2[i]
    if a == b:
        print("bad")
        sys.exit()
    if a in dc:
        if b != dc[a]:
            print("bad")
            sys.exit()
    if b in dc:
        if a != dc[b]:
            print("bad")
            sys.exit()
    dc[a] = b

print("good")
