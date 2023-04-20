# 1이 될때 까지 99p
a, b = map(int, input().split())
count = 0

while a != 1:
    if a % b == 0:
        a = a / b
        count += 1
    else:
        a -= 1
        count += 1

print(count)

# N이 k의 배수가 되도록 효율적으로 한번에 뺴는 방식

# N, K공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
