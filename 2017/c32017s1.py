import sys

n = int(sys.stdin.readline())
swifts = [int(x) for x in sys.stdin.readline().split()]
semaphores = [int(x) for x in sys.stdin.readline().split()]

k = 0
x = 0

swifts_k = 0
semaphores_k = 0

zero = True

for r in range(0,n):
    swifts_k += swifts[r]
    semaphores_k += semaphores[r]

    if swifts_k == semaphores_k and swifts_k > k and semaphores_k > k:
        k = swifts_k
        x = r
        zero = False

if zero == True:
    print 0
if zero == False:
    print x + 1
