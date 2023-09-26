# 제목: 중첩 for반복문을 활용하여 입력한 n단까지 구구단 출력하기
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.09.26

n = int(input("n을 입력하세요."))

for i in range(1, 10):
    for j in range(2, n+1):
        gugudan = f"{j}*{i}={j*i}"
        print(gugudan, end="\t")
    print()
