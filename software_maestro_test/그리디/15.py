# 기타줄
n, m = map(int, input().split())
data = []
res = 0

for i in range(m):
    a, b = map(int, input().split())
    data.append([a, b])

data1 = sorted(data, key=lambda x: x[0])  # [[20, 8], [40, 7], [60, 4]]
data2 = sorted(data, key=lambda x: x[1])  # [[60, 4], [40, 7], [20, 8]]

if data1[0][0] <= data2[0][1]*6:
    a = n//6
    arg = n - 6*a
    res = data1[0][0] * (n//6) + data2[0][1] * arg
    # 그냥 6개 패키지를 사는게 더 가격이 쌀 경우가 있는데 이럴 때는 그냥 6개 패키지를 하나 더산다.
    if data1[0][0] < data2[0][1] * arg:
        res = data1[0][0] * (n//6 + 1)
else:
    res += data2[0][1] * n

print(res)
