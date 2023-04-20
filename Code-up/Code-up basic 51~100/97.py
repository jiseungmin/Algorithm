from posixpath import split


h,w = map(int, input().split())
n = int(input())
array = []

for i in range(h):
  array.append([])
  for j in range(w):
    array[i].append(0)

for i in range(n):
  l,d,x,y= map(int,input().split())
  if(d==0):
    for i in range(0,l):
      array[int(x-1)][int(y+i-1)]=1
  if(d==1):
    for j in range(0,l):
      array[int(x-1+j)][int(y-1)]=1

for i in range(0,h):
  for j in range(0,w):
    print(array[i][j],end=' ')
  print()  