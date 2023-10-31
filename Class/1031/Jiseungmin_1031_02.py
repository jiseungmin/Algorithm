# 제목:  버블 정렬 with ChatGPT
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.31

import random
number = [i for i in range(1,11)]
random.shuffle(number)
print("임의의 순서로 출력된 1부터 10까지의 수: ", number)

# 버블정렬로 내림차순 출력
for i in range(len(number)-1):
  for j in range(len(number)-i-1):
    if number[j] < number[j+1]:
      number[j], number[j+1] = number[j+1], number[j]

print("버블정렬로 내림차순으로 정렬된 1부터 10까지의 수:", number)

