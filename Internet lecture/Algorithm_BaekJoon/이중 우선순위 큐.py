# . ‘I n’은 정수 n을 Q에 삽입하는 연산을 의미
# D 1’는 Q에서 최댓값을 삭제하는 연산
# D -1’는 Q 에서 최솟값을 삭제하는 연산을 의미

import heapq

n = int(input())
m = int(input())
heap = []

for i in range(2):
    for i in range(m):
        q, t = map(int, input().split())
        if(q == 'I'):
            heap.append(t)
        elif q == 'D':
            if t == 1:
                heap.remove(max(heap))
            elif t == -1:
                heap.remove(min(heap))

if len(heap) == 0:
    print("EMPTY")
else:
    print(heap)
