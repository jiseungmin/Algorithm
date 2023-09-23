import sys

input = sys.stdin.readline

n = int(input())
result = []

for i in range(n):
    m = int(input())
    if m == 0:
        result.pop()
    else:
        result.append(m)

print(sum(result))
