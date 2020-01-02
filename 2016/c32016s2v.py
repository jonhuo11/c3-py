# verified by DMOJ

q_type = int(input())
amt = int(input())
d_speeds = [int(item) for item in input().split()]
p_speeds = [int(item) for item in input().split()]

ret = 0
if q_type == 1:
    d_speeds = sorted(d_speeds)
    p_speeds = sorted(p_speeds)

    for i in range(0, len(d_speeds)):
        ret += max(d_speeds[i], p_speeds[i])
else:
    d_speeds = sorted(d_speeds, reverse=True)
    p_speeds = sorted(p_speeds)

    for i in range(0, len(d_speeds)):
        ret += max(d_speeds[i], p_speeds[i])

print(ret)
