n = 16
k = 4

count = 0

while(True):
    if n == 1:
        break

    if n % k == 0:
        count += n/k
        n = n % k
    else:
        count += 1
        n = n-1

print(count)
