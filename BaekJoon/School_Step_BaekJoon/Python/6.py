a = int(input())
data = []
count =0

for i in range(a):
    s = input()
    data.append(s)

for i in data :
    for j in data :
        if i == j :
            count += 1

print(a-count)