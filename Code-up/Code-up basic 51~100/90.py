from posixpath import split


a,b,c,d = map(int,input().split())
cnt = a
for i in range(1,d):
  cnt = cnt * b + c
  result = cnt
print(cnt)