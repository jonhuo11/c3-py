# determine rotation by finding the corner with the smallest number
# 4 cases for each possible corner

n = int(input())
rows = []
for r in range(n):
    rows.append([int(x) for x in input().split()])

# find the corner with smallest number
li = [rows[0][0], rows[0][n-1], rows[n-1][n-1], rows[n-1][0]]
corner = li.index(min(li))

def print_arr(arr):
    out = str(arr[0])
    for i in range(1, len(arr)):
        out += " " + str(arr[i])
    print(out)

# conditions
if corner == 0:
    # return the input since there is no difference
    for row in rows:
        r = str(row[0])
        for i in range(1, len(row)):
            r += " " + str(row[i])
        print(r)
elif corner == 1:
    # start at rightmost column, convert into rows
    for i in sorted(list(range(n)), reverse=True):
        col = []
        for r in rows:
            col.append(r[i])
        print_arr(col)
elif corner == 2:
    # start at bottom row, print reversed rows
    rows.reverse()
    for row in rows:
        row.reverse()
        print_arr(row)
elif corner == 3:
    # start at leftmost column, print reversed column
    rows.reverse()
    for i in range(n):
        col = []
        for row in rows:
            col.append(row[i])
        print_arr(col)
