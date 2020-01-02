# verified by DMOJ

t = int(input())
ns = 1
outs = []
while ns <= t:
    ns += 1
    n = int(input())
    mt = [int(input()) for x in range(n)]
    br = []
    last = 0
    while True:
        if (len(mt) < 1 and len(br) == 1) or (len(br) < 1 and len(mt) == 1):
            outs.append("Y")
            break
        elif len(mt) > 0 and mt[-1] == last + 1:
            last = mt[-1]
            mt.pop(-1)
        elif len(br) > 0 and br[-1] == last + 1:
            last = br[-1]
            br.pop(-1)
        elif len(mt) > 0:
            br.append(mt.pop(-1))
        else:
            outs.append("N")
            break
for o in outs:
    print(o)
