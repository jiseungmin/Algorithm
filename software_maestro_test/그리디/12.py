# 신입 사원
import sys

n = int(input())

for i in range(n):
    a = int(input())
    data = [list(map(int, sys.stdin.readline().strip().split()))
            for i in range(a)]
    data.sort()

    cnt = 1
    min = data[0][1]

    for i in range(0, a):
        if data[i][1] < min:
            min = data[i][1]
            cnt += 1

    print(cnt)
