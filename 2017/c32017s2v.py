# verified by DMOJ

import math

n = int(input())
tides = sorted([int(x) for x in input().split()])

lows = sorted(tides[:math.ceil(len(tides)/2)], reverse=True)
highs = tides[math.ceil(len(tides)/2):]

out = []
if len(lows) > len(highs):
    out.append(lows.pop(0))

    for i in range(len(lows)):
        out.append(highs[i])
        out.append(lows[i])
else:
    for i in range(len(highs)):
        out.append(lows[i])
        out.append(highs[i])

s = ""
for c in out:
    s += str(c) + " "
print(s[:-1])
