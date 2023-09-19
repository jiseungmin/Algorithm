# 제목: 정수 n의 제곱 계산
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.09.19

def compute_square_A(n):
    count = 0
    count += 1
    return n*n, count


def compute_square_B(n):
    sum = 0
    count = 0
    for i in range(n):
        sum = sum + n
        count += 1
    return sum, count


def compute_square_C(n):
    sum = 0
    count = 0
    for i in range(n):
        for j in range(n):
            sum = sum + 1
            count += 1
    return sum, count


n = int(input("정수 n을 입력하세요: "))

print("알고리즘 A 결과:%d 횟수:%d" %
      (compute_square_A(n)[0], compute_square_A(n)[1]))
print("알고리즘 B 결과:{:d} 횟수:{:d}".format(
    compute_square_B(n)[0], compute_square_B(n)[1]))
print(f"알고리즘 C 결과:{compute_square_C(n)[0]} 횟수:{compute_square_C(n)[1]}")
