# 제목: 교환 가능 동전 개수
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.09.26

money, c500, c100, c50, c10 = 0, 0, 0, 0, 0
money = int(input("교환하고자 하는 금액은? "))

c500 = money//500
money %= 500

c100 = money//100
money %= 100

c50 = money//50
money %= 50

c10 = money//10
money %= 10

print("\n500원 짜리: %d 개" % c500)
print("\n100원 짜리: %d 개" % c100)
print("\n 50원 짜리: %d 개" % c50)
print("\n 10원 짜리: %d 개" % c10)
print("\n      잔돈: %d 개" % money)
