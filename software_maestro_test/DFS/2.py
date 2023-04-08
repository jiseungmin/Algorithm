# 미로 탈출

from collections import deque

n, m = map(int, input().split())
data = []

for i in range(n):
    data.append(list(map(int, input())))

# 이동할 네방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌떄까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if data[nx][ny] == 0:
                continue

            if data[nx][ny] == 1:
                data[nx][ny] = data[x][y]+1
                queue.append((nx, ny))
    return data[n-1][m-1]


print(bfs(0, 0))
