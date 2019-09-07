out = []
def solve(current, st):
    # the current jersey numbers being used, st of useable jersey numbers, depth of recursion
    # base cases: if the depth is reached or not enough numbers left to use
    if len(current) == 4:
        return current
    elif (len(current) < 4) and len(st) == 0:
        return None
    else:
        # at each number, we can either choose to use the next number or not
        u, u1 = current.copy(), st.copy()
        n = st.copy()
        # use
        u.append(st[0])
        u1.pop(0)
        # not use: skip next
        n.pop(0)
        global out
        out.append(solve(u, u1))
        out.append(solve(current, n))
j = int(input())
solve([j], sorted(list(range(1, j)), reverse=True))

n = 0
for o in out:
    if o != None:
        n += 1
print(n)
