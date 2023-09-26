# 제목: for문 피라미드 출력하기
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.09.26

n = int(input(""))

for i in range(0, n+1):
    for j in range(i):
        print("*", end="")
    print()

print("----------------------")

for i in range(0, n):
    for k in range(1, n-i):
        print(" ", end='')
    for j in range(0, i*2+1):
        print("*", end='')
    print()
