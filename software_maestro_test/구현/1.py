# 왕실의 나이트
n = input()
x = int(ord(n[0])) - int(ord('a')) + 1
y = int(n[1])

count = 0

movement = [(2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)]

for dx, dy in movement:
    next_x = dx+x
    next_y = dy+y
    if next_x >= 1 and next_x <= 8 and next_y >= 1 and next_y <= 8:
        count += 1

print(count)
