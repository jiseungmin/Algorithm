# 제목:  외판원 순회
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.12

import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())

matrix = [list(map(int,input().split())) for _ in range(n)]
answer = 1000000

for i in permutations(range(1,n), n-1):
  num_list = [*i]

  #처음과 끝에 1번 도시를 넣는다.
  num_list = [0] + num_list + [0]
  sub = 0

  for j in range(n):
    cost = matrix[num_list[j]-1][num_list[j+1]-1]
    if cost == 0 :
      break
    else :
      sub += cost
    
    if sub > answer :
      break
  else:
        if answer > sub :
          answer = sub
print(answer)

