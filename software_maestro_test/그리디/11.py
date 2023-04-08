# 회의실 배정

n = int(input())
q = []
cnt = 0

for i in range(n):
    a, b = map(int, input().split())
    q.append([a, b])

q = sorted(q, key=lambda x: x[0])
q = sorted(q, key=lambda x: x[1])

last = 0
for i, j in q:
    if i >= last:
        cnt += 1
        last = j

print(cnt)

print(q)
