# 제목: 자연수 2진수 변환
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.09.26

import math
count = 0


def binary_digits(n):
    global count
    count += 1

    if n == 1:
        return 1
    else:
        return 1 + binary_digits(n//2)


n = int(input("자연수 n를 입력하세요."))
print(f"총 비트 수 (100) = {binary_digits(n)}")
print(f"함수 호출 횟수 : {count}")
print(f"log2({n})은 {math.log2(n):.4f}")
