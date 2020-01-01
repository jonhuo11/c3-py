# verified by DMOJ

n = int(input())
right = []
response = []
for i in range(n):
    right.append(input())
for i in range(n):
    response.append(input())

counter = 0
for i in range(len(right)):
    if right[i] == response[i]:
        counter += 1

print(counter)
