n , m= map(int, input().split())
data = list(map(int, input().split()))

result = 0
lenght = len(data)

for i in range(0,lenght) :
    for j in range(i+1,lenght) :
        for k in range(j+1, lenght):
            sum_value = data[i]+data[j]+data[k]
            if sum_value <= m :
                result = max(result, sum_value)
       
print(result)
     
