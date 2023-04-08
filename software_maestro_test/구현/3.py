# 럭키 스트레이트 풀이
n = input()

a = n[:int(len(n)/2)]
b = n[int(len(n)/2):]

res1 = 0
res2 = 0

for i in a:
    res1 += int(i)

for i in b:
    res2 += int(i)


if res1 == res2:
    print("LUCKY")
else:
    print("READY")
