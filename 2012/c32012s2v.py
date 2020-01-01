# verified by DMOJ

mp = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

st = list(input())

sum = 0
i = 0
while i < len(st):
    # two cases: R1 is bigger than R, R1 is smaller than R
    if i + 3 < len(st) and mp[st[i + 3]] > mp[st[i + 1]]:
        sum -= (int(st[i]) * mp[st[i + 1]])
    else:
        sum += (int(st[i]) * mp[st[i + 1]])
    i += 2

print(sum)
