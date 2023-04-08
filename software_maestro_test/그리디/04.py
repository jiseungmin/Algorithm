# 모험가 길드 문제
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
cnt = 0

for i in data:
    cnt += 1
    if cnt >= i:
        cnt = 0
        result += 1

print(result)
