# verified by DMOJ
n = int(input())

nums = []
for x in range(0, n):
    y = int(input())
    if y != 0:
        nums.append(y)
    else:
        nums.pop()

out = 0
for x in nums:
    out += x

print(out)
