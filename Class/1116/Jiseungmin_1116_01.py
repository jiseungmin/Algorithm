# 제목: 퀵 정렬
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.11.16

def quick_sort(A, left, right):
  if left < right :
    mid = partition(A,left, right)
    quick_sort(A, left, mid-1)
    quick_sort(A, mid+1, right)

def partition(A,left, right):
  low = left + 1
  high = right
  pivot = A[left]
  while (low <= high) :
    while low <= right and A[low] < pivot : low +=1
    while high >= left and A[high] > pivot : high -= 1

    if low < high :
      A[low], A[high] = A[high], A[low]
  
  A[left], A[high] = A[high], A[left]
  return high

data = [5,3,8,4,9,1,6,2,7] 
print("Original : ", data)
quick_sort(data, 0, len(data)-1)
print("QuickSort : ", data)
