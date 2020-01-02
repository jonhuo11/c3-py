# verified by DMOJ

n = int(input())
vs = sorted([int(input()) for x in range(n)])
hoods = []

for i in range(1, len(vs) - 1):
    left = abs(vs[i] - vs[i - 1])/2
    right = abs(vs[i + 1] - vs[i])/2
    hoods.append(right + left)

print(round(min(hoods), 1))
