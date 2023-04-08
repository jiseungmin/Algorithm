# A->B
import sys
n, m = map(int, sys.stdin.readline().split())
count = 1

while True:
    if m == n:
        break
    if m < n:
        count = -1
        break
    elif m % 2 == 0:
        m = m//2
        count += 1
    elif m % 10 == 1:
        m = m//10
        count += 1
    else:
        count = -1
        break

print(count)
