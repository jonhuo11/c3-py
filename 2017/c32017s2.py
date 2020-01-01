'''
import math

n = int(input())
measures = sorted([int(x) for x in input().split()], reverse=True)
m1 = measures

ret = []

if len(m1) % 2 == 0:
    while len(m1) > 0:
        ret.append(m1[0])
        m1.pop(0)
        try:
            ret.append(m1[len(m1)-1])
            m1.pop()
        except IndexError as e:
            pass
else:
    x = m1.pop(int(math.ceil(len(m1)/2)))
    while len(m1) > 0:
        ret.append(m1[len(m1)-1])
        m1.pop()
        try:
            ret.append(m1[0])
            m1.pop(0)
        except IndexError as e:
            pass
    ret.append(x)

if len(m1) % 2 == 0:
    ret.reverse()

out = ""
for x in ret:
    out += str(x)
    out += " "

print(out)
'''
