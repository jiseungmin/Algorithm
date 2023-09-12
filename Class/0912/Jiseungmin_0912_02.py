# 제목 : 유클리드 호재법을 이용한 최대공약수 찾기(DP)
# 이름 : 컴퓨터 공학부 지승민
# 날짜 : 2023.09.12

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = int(input("첫번쨰 정수를 입력하세요"))
b = int(input("두번쨰 정수를 입력하세요"))

print("최대공약수는", gcd(a, b), "입니다.")
