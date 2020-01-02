# verified by DMOJ

# pretty average primes

import math

t = int(input())
ns = [int(input()) for x in range(t)]
outs = []

def is_prime(n):
    for i in range(2, round(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

for n in ns:
    for i in range(2 * n):
        a = i
        b = 2 * n - i
        if (a != 1 and b != 1) and is_prime(a) and is_prime(b) and a + b == 2 * n:
            outs.append((a, b))
            break

for out in outs:
    print(out[0], out[1])
