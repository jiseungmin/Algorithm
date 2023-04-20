a = int(input())
b = input().split()
array = []

for i in range(0,len(b)):
  array.append(b[i])

array.reverse()
for i in range(0,len(b)):  
 print(array[i],end=' ')
