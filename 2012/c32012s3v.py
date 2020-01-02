# verified by DMOJ
n = int(input())
rs = [int(input()) for x in range(n)]
dc = {}
highest = 1
for r in rs:
    if r in dc:
        dc[r] += 1
        if dc[r] > highest:
            highest = dc[r]
    else:
        dc[r] = 1

hs = []
hs2 = []
for k in dc:
    if dc[k] == highest:
        hs.append(k)
        dc[k] = -1

highest2 = 1
for k in dc:
    if dc[k] > highest2:
        highest2 = dc[k]
for k in dc:
    if dc[k] == highest2:
        hs2.append(k)

if len(hs) >= 2:
    z = sorted(hs)
    print(abs(z[-1] - z[0]))
elif len(hs) == 1 and len(hs2) == 1:
    print(abs(hs[0] - hs2[0]))
else:
    print(max(abs(sorted(hs)[0] - sorted(hs2)[0]), abs(sorted(hs)[0] - sorted(hs2)[-1])))
