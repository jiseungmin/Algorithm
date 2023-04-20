# 해설 코드
a, b = map(int, input().split())

result = 0
while True :
  target = (a//b) * b
  result += (a - target)
  a = target
  if a< b:
    break
  result += 1
  a //= b

result += (a-1)
print(result) 