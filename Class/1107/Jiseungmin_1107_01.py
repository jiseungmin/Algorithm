# 제목: 선형 탐색(성능)
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.11.02

import random

numList = [1,5,7,13,50,120,300,320,400,700]

for k in range(20):
  cntSum = 0
  for i in range(10000):
    rndNum = numList[random.randint(0,9)]
    for n in numList:
      cntSum += 1
      if n == rndNum:
        break
  print(cntSum/10000)