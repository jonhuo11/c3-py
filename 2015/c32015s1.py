import sys

n = int(sys.stdin.readline())

nums = []
for x in range(0, n):
    y = int(sys.stdin.readline())
    if y != 0:
        nums.append(y)
    else:
        nums.pop()

out = 0
for x in nums:
    out += x

print(out)
