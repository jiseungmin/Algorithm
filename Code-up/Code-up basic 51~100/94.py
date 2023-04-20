a = int(input())
b = input().split()
array = []
for i in range(0,a):
  array.append(int(b[i]))

array.sort()
print(array[0])