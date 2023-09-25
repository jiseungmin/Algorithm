result = []

for i in range(0, 5):
    data = list(map(int, input().split()))
    result.append((i+1, sum(data)))

result = sorted(result, key=lambda x: x[1])
print(result[-1])
