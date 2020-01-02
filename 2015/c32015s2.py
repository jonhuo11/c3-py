# on DMOJ, this passes with a score of 12/15. Last test case runs over time for some reason

# if it fits, give immediately
j = int(input())
a = int(input())

jerseys = []

for i in range(j):
    r = 0
    st = input()
    if st == "S":
        r = 1
    elif st == "M":
        r = 2
    else:
        r = 3
    jerseys.append(r)

out = 0
for i in range(a):
    r = 0
    st = input()
    if st[0] == "S":
        r = 1
    elif st[0] == "M":
        r = 2
    else:
        r = 3

    if jerseys[int(st[2]) - 1] >= r:
        out += 1
        jerseys[int(st[2]) - 1] = -1

print(out)
