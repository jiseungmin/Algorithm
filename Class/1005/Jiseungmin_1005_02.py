# 제목: lamda기초 - 익명함수와 일반 함수의 차이
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.05

def power_l(x): return x*x


def power_func(a):
    res = a*a
    return res


num = int(input("제곱을 구하고자 하는 숫자를 입력: "))
result = power_func(num)
result2 = power_l(num)

print(f"{num}의 제곱f은 {result}이다. ")
print(f"{num}의 제곱l은 {result2}이다. ")
