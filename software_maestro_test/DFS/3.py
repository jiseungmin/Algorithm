# 특정거리의 도시찾기
from collections import deque

n, m, k, x = map(int, input().split())
data = [[]for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b)


def bfs(k, x):
    que = deque([x])
    visited[x] = 0
    city = []

    while que:
        x = que.popleft()
        for y in data[x]:
            if visited[y] == -1:
                visited[y] = visited[y] + 1
                que.append(y)

                if visited[y] == k:
                    city.append(y)
                elif visited[y] > k:
                    return city
        return city


visited = [-1] * (n+1)
city = bfs(k, x)

if city:
    for x in sorted(city):
        print(x)
else:
    print(-1)
