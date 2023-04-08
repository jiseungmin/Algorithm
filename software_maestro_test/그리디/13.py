# 카드 정렬하기
import heapq

q = []
result = 0

for i in range(int(input())):
    heapq.heappush(q, int(input()))

if len(q) == 1:
    print(0)
else:
    while len(q) > 1:
        plus = heapq.heappop(q) + heapq.heappop(q)
        result += plus
        heapq.heappush(q, plus)
    print(result)
