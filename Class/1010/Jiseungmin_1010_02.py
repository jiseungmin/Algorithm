# 제목: 선택 정렬 with python
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.10

def selection_sort(a):
  n = len(a)
  for i in range(n-1):
    least = i
    for j in range(i+1,n):
      if(a[j]<a[least]):
        least = j
    a[i], a[least] = a[least], a[i]
    printStep(a,i+1)

def printStep(arr, val):
  print(" Step%2d = " %val, end='')
  print(arr)

data= [5,3,8,4,9,1,6,2,7]
print("Original : ", data)
selection_sort(data)
print("Selection : ", data)