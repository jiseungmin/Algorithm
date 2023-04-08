# 곱하기 혹은 더하기
n = input()
result = n[0]

for i in n:
    if int(i) == 0 or int(i) == 1:
        result += int(i)
    else:
        result *= int(i)

print(result)
