# this solution does not score full points on DMOJ because it is too slow
# TODO: fix the time complexity from O(n**4) to O(n**3)

# combining riceballs

n = int(input())
rb = [int(x) for x in input().split()]

def try_combine(i, j, a):
    # check if items from i to j can be combined
    if j < len(a) and a[i] == a[j] and abs(j - i) < 3:
        return combine(i, j, a)
    return max(a)

def combine(i, j, a1):
    a = a1.copy()
    sum = 0
    for x in range(i, j + 1):
        sum += a[x]
    a[i] = sum
    del a[i + 1:j + 1]
    return a

dp = {}
def solve(r, i):
    key = str(r) + ":" + str(i)
    global dp
    if key in dp:
        return dp[key]
    elif type(r) == int:
        dp[key] = r
    elif i < len(r):
        dp[key] = max(solve(try_combine(i, i + 1, r), 0), solve(try_combine(i, i + 2, r), 0), solve(r, i + 1))
    else:
        dp[key] = max(r)
    return dp[key]

print(solve(rb, 0))
