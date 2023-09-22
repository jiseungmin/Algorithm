a = int(input())
a_data = set(map(int, input().split()))
b = int(input())
b_data = list(map(int, input().split()))
count = 0

for value in b_data:
    if value not in a_data:
        print("0")
    else:
        print("1")
