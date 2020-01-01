# verified correct by DMOJ

actions = list(input())
arr = [1,2,3,4]

for a in actions:
    old = arr.copy()
    if a == "H":
        arr[0] = old[2]
        arr[1] = old[3]
        arr[2] = old[0]
        arr[3] = old[1]
    if a == "V":
        arr[0] = old[1]
        arr[1] = old[0]
        arr[2] = old[3]
        arr[3] = old[2]

print("{} {}".format(arr[0], arr[1]))
print("{} {}".format(arr[2], arr[3]))
