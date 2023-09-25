from collections import deque
import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))
answer = 0

bridge = deque([0 for _ in range(w)])

while trucks:
    bridge.popleft()
    if len(bridge) < w:
        if sum(bridge) + trucks[0] <= l:
            truck = trucks.popleft()
            bridge.append(truck)
        else:
            bridge.append(0)
    answer += 1
answer += w
print(answer)
