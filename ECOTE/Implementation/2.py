# 왕실의 나이트
input = input()
row = int(input[1])
column = int(ord(input[0]))-int(ord('a'))+1

# R R U D
plan = [(-2, 1), (-2, -1), (2, -1), (2, 1), (1, -2), (-1, -2), (1, 2), (1, -2)]

result = 0

for step in plan:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1


print(result)
