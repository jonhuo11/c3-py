import sys

g = int(sys.stdin.readline())
p = int(sys.stdin.readline())

gates = [False for x in range(0,g)]

planes = [int(sys.stdin.readline()) for x in range(0,p)]

planes = sorted(planes)
amt = 0
last = None
for p in range(0,len(planes)):
    if planes[p] == last:
        continue
    last = planes[p]
    for i in range(0,planes[p]):
        if gates[i] == False:
            gates[i] = True
            amt += 1
            break

print amt
