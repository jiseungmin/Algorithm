# 숫자 카드 게임
n, m = map(int, input().split())
arr = []
arr2 = []

for i in range(n):
    arr = list(map(int, input().split()))
    arr2.append(min(arr))

print(max(arr2))
