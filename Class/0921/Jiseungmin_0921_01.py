# 제목: 자연수 2진 변환
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.09.21

import math


def binary_digits(n):
    count = 1
    while n > 1:
        count = count + 1
        n = n // 2
    return count


n = int(input("자연수 n을 입력하세요: "))
print(f"총 비트수 ({n}) = {binary_digits(n)}")
print(f"log2({n})은 {math.log2(n):.4f}")
