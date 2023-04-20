# 숫자 카드 게임 98p
a, b = map(int, input().split())
result = 0

for i in range(a):
    data = list(map(int, input().split()))
    data.sort()
    result = data[i]
    if data[i] > result:
        result = data[i]
    data = []

print(result)

# min() 함수를 이용하는 답안 예시
n, m = map(int, input().split())
result = 0

for i in range(i):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

# 2중 반복문 구조를 이용하는 답안 예시
n, m = map(int, input().split())
result = 0

for i in range(i):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)
