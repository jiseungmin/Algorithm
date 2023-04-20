# 두 배열의 원소 교체
a,b = map(int, input().split())

Aarray = list(map(int, input().split()))
Barray = list(map(int, input().split()))

Aarray.sort()
Barray.sort(reverse=True)

for i in range(b):
  if Aarray[i] < Barray[i]:
    Aarray[i], Barray[i] = Barray[i], Aarray[i]
  else:
    break

print(sum(Aarray))    