# scores correctly on some test cases on DMOJ, more work needed

# calculate least number of days
# where do you use the shorter day (remainder)?
ln1 = input().split()
n = int(ln1[0])
k = int(ln1[1])

attr = [int(x) for x in input().split()]

rem = n % k

def solve(a, r, o):
    # 2 branches, either you can use the r now or save it
    # if r is used, it is -1
    if len(a) < 1:
        return 0
    elif r == -1 or r == 0:
        sum = 0
        for x in range(0, len(a), o):
            sum += max(a[x:x + o])
        return sum
    else:
        if len(a) == r:
            return max(a)
        else:
            # return max(solve(without r), solve(with r))
            return max(max(a[:o]) + solve(a[o:], r, o), max(a[:r]) + solve(a[r:], -1, o))

print(solve(attr, rem, k))
