# 제목:  삽입정렬
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.31

def insertion_sort(A):
  n = len(A)
  for i in range(1,n):
    key = A[i]
    j =  i -1
    while j>=0 and A[j] > key:
      A[j+1] = A[j]
      j = j - 1
    A[j+1] = key
    printStep(A,i)

def printStep(arr, val):
  print(" Step %2d= " %val, end='')
  print(arr)

data = [5,3,8,4,9,1,6,2,7]
print("Original: ",data)
insertion_sort(data)
print("Insertion: ", data)
      

