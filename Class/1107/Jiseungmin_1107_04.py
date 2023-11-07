# 제목: 이진 탐색 반복문
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.11.02

def binary_search(array, target, start, end):
  while start <= end :
    mid = (start+end)//2
     
    if array[mid] == target :
        return mid
    elif array[mid] > target :
        end = mid -1
    else : 
        start = mid +1
  return None

n,target = list(map(int,input().split()))
array = list(map(int,input().split()))

result = binary_search(array, target, 0, n-1)
if result == None :
  print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

