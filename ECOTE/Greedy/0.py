 # 1이 될떄까지
 # 해설 보기전 내 코드
a, b = map(int, input().split())
cnt = 0
while True :
  if(a==1):
    break
  else:  
    if(a%b ==0):
      a = a/b
      cnt += 1
    else:
      a-=1
      cnt += 1
print(cnt)  


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

   