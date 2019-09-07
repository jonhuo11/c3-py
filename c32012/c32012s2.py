map = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

def calc(pair):
    return (int(pair[0]) * (map[pair[1]]))

num = list(input())

grouped = []
i = 1
while (i < len(num)):
    grouped.append([num[i-1], num[i]])
    i += 2
output = calc(grouped[0])
for i in range(1, len(grouped)):
    pair = grouped[i]
    last_pair = grouped[i-1]
    if map[pair[1]] > map[last_pair[1]]:
        output += calc(pair)
    else:
        output -= calc(pair)
print(output)
