n = int(input())
data = {}
result = []

for i in range(n):
    m = int(input())
    for i in range(m):
        fr1, fr2 = input().split()
        if fr1 not in data:
            data[fr1] = 1
        else:
            data[fr1] += 1

        if fr2 not in data:
            data[fr2] = 1
        else:
            data[fr2] += 1
        result.append(data[fr1]+data[fr2])


print(result)
