# 주유소 문제
n = int(input())  # 4
lenght = list(map(int, input().split()))  # 3 3 4
sum_len = sum(lenght)  # 3
money = list(map(int, input().split()))  # 1 1 1


res = money[0]*lenght[0]  # 10
sum_len -= lenght[0]

money.sort()

res += sum_len*money[1]

print(res)


n = int(input())
cities = list(map(int, input().split()))
prices = list(map(int, input().split()))

ans = 0
min_price = prices[0]

for i in range(n-1):
    if prices[i] < min_price:
        min_price = prices[i]

    ans += min_price * cities[i]

print(ans)
