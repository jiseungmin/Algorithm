from collections import deque

n, k = map(int, input().split())
d = deque([i for i in range(1, n)])
result = []

for i in range(n):
    # k-1 번 왼쪽으로 돌리기 수행
    for i in range(k-1):
        x = d.popleft()
        d.append(x)
    x = d.popleft()
    result.append(x)

print('<', end='')
for i in range(len(result)):
    if i < len(result) - 1:
        print(result[i], end=',')
    else:
        print(result[i], end='')
print('>')
