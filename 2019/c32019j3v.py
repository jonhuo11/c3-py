# verified by DMOJ

n = int(input())

outs = []

# n rows of text
for row in range(n):
    # encode each row
    s = input()
    out = ""
    prev = s[0]
    counter = 0
    for c in s:
        if c != prev:
            # if c not prev, set prev to c and add to the encoding, reset counter
            out += str(counter) + " " + prev + " "
            prev = c
            counter = 1
        else:
            counter += 1
            prev = c
    out += str(counter) + " " + prev
    outs.append(out)

for out in outs:
    print(out)
