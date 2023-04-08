# 연산자 끼워넣기
index = 0
result = []
n = int(input())
data = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
booho = []

for i in range(a):
    booho.append("+")
for i in range(b):
    booho.append("-")
for i in range(c):
    booho.append("*")
for i in range(d):
    booho.append("/")

for i in booho:
    if i == "+":
        result.append(data[index]+data[index+1])
        index += 1
    elif i == "-":
        result.append(data[index]-data[index+1])
        index += 1
    elif i == "*":
        result.append(data[index]*data[index+1])
        index += 1
    elif i == "/":
        result.append(data[index]/data[index+1])
        index += 1




print(max(result))
print(min(result))
