# 큰수의 법칙 이코테 92p

a, b, c = map(int, input().split())
data = list(map(int, input().split()))
result = 0
count = 0

data.sort()

while(True):
    if count == b:
        break
    for i in range(c):
        result += data[a-1]
        count += 1
    if count == b:
        break
    result += data[a-2]
    count += 1
print(result)

# 간단한 수학적 아이디어를 이용해 효율적으로 처리
a, b, c = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
count = int(b/(c+1)*c)
count += b % (c+1)

result = 0
result += count * data[a-1]
result += (b-count) * data[a-2]
print(result)
