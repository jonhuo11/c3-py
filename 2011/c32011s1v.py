# verified correct by DMOJ

n = int(input())
lines = []
for i in range(n):
    lines.append(input())

t_count = 0
s_count = 0

for ln in lines:
    for c in ln:
        if c == "s" or c == "S":
            s_count += 1
        elif c == "t" or c == "T":
            t_count += 1

if t_count > s_count:
    print("English")
else:
    print("French")
