# 제목:  큐 with python
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.19
from collections import deque

queue = deque()
# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)




