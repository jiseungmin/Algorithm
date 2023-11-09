# 제목: 퀵 정렬(파이썬 장점을 살린 방식
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.11.09

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
  if len(array) <= 1:
    return array
  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort(left_side)+ [pivot] + quick_sort(right_side)

print(quick_sort(array))