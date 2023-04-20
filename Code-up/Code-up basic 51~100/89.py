a,b,c = map(int,input().split())
cnt = a
for i in range(1,c):
  
  cnt = cnt * b
  result = cnt
  
print(result)