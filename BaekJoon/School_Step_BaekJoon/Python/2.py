s = input() #baekjoon
data = [] #noojkeab
for i in s[::-1] :
    data.append(i);

if data[0] == s[0]:
    print(1)
else:
    print(0)