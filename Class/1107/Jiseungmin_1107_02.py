# 제목: 이진 탐색(성능)
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.11.02

import random

numList = [1,5,7,13,50,120,300,320,400,700]

for k in range(20):
  cntSum = 0
  for i in range(10000):
    start = 0
    end = len(numList) - 1
    key = int((start+end) /2)
    V = random.randint(start,end)
    while True :
      cntSum += 1
      if numList[key] == numList[V] or start == end :
        break
      elif numList[key] < numList[V]:
        start = key +1
        key = int((start + end)/ 2)
      else:
        end = key -1
        key =int((start+end)/2)
        
  print(cntSum/10000)
