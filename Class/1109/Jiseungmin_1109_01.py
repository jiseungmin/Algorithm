# 제목: 가짜 동전을 찾아내는 순차탐색 알고리즘
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.11.09

def weigh(a,b,c,d):
  fake = 29
  if a < fake and fake <= b:
    return -1
  if c <= fake and fake <= d:
    return 1
  return 0

def find_fakecoin(left, right):
  for i in range(left + 1 ,right +1):
    result = weigh(left, left, i , i)
    if result == -1 :
      return left
    elif result == 1:
      return i
  
  return -1

n = 100
print(find_fakecoin(0, n-1))