# 제목:  순차 탐색 with python
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.10

def sequential_search(A,key):
  for i in range(len(A)):
    if A[i] == key:
      return i+1
  return -1

A = [32,14,5,17,23,9,11,4,26,29]

print(f"리스트 A: {A}")
print(f"리스트 A 크기: {len(A)}")
num = int(input("찾고자 하는 수 입력:"))
print(f"순차 탐색 횟수: {sequential_search(A,num)}")