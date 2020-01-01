'''
j = int(input())
a = int(input())

jerseys = []
requests = []

for i in range(0,j):
    s = input().split()[0]
    r = 0
    if s == "S":
        r = 1
    if s == "M":
        r = 2
    if s == "L":
        r = 3
    jerseys.append([r, i+1])

for i in range(0,a):
    s = input().split()
    r = 0
    if s[0] == "S":
        r = 1
    if s[0] == "M":
        r = 2
    if s[0] == "L":
        r = 3
    requests.append([r, int(s[1])])

amt = 0
for re in requests:
    for je in jerseys:
        if je[1] == re[1] and je[0] >= re[0]:
            amt += 1

print(amt)
'''
