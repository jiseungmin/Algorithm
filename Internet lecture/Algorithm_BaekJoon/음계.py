n = list(map(int, input().split(' ')))

ascending = True
desecnding = True

for index in range(1, len(n)):
    if n[index] > n[index-1] :
        desecnding = False
    elif n[index] < n[index-1] :
        ascending = False


if ascending:
    print("ascending")
elif desecnding :
    print("descending")
else :
    print("mixed")
    
    