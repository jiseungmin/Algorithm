# 큰수의 법칙
a, b, c = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
result = 0

arr.sort(reverse=True)

for i in range(b):
    if(cnt < c):
        result += arr[0]
        print(result)
        cnt += 1
    else:
        result += arr[1]
        cnt = 0

print(result)
