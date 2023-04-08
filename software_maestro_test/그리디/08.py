# 볼링공 고르기
n, m = map(int, input().split())
data = list(map(int, input().split()))

a = []

for i in range(len(data)):
    for j in range(len(data)):
        if data[i] != data[j]:
            a.append([data[i], data[j]])

print(len(a)//2)


import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
balls = list(map(int, sys.stdin.readline().rstrip().split()))

# 무게별 볼링공의 개수 정리
weights = [0] * 10
for ball in balls:
    weights[ball] += 1

# 조합 결과
result = 0

# 조합 계산
for i in range(n):
    # i번째 무게보다 높은 무게의 볼링공 개수
    n -= weights[i]
    # i번째 무게의 볼링공 개수 * i번째 무게보다 높은 무게의 볼링공 개수
    result += weights[i] * n

print(result)