# Author : @jonathanhuo11
# Description : Problem S2 Solution, in Python

import sys
import re

q_type = int(sys.stdin.readline())
amt = int(sys.stdin.readline())
d_speeds = [int(item) for item in sys.stdin.readline().split()]
p_speeds = [int(item) for item in sys.stdin.readline().split()]

ret = 0
if q_type == 1:
    d_speeds = sorted(d_speeds)
    p_speeds = sorted(p_speeds)

    for i in range(0, len(d_speeds)):
        ret += min(d_speeds[i], p_speeds[i])
else:
    d_speeds = sorted(d_speeds, reverse=True)
    p_speeds = sorted(p_speeds)

    for i in range(0, len(d_speeds)):
        ret += max(d_speeds[i], p_speeds[i])

print ret
