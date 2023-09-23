import sys
n = int(sys.stdin.readline())
stack = []
result = []
current = 1

for _ in range(n):
    x = int(input())
    while len(stack) == 0 or stack[-1] < x:
        stack.append(current)
        current += 1
        result.append('+')
    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        result = ['No']
        break

for x in result:
    print(x)
