# 제목 : 2차방정식의 근의 해
# 이름 : 지승민
# 날짜 : 2023.09.07
import math


def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2*a)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2


answer = solve_quadratic_equation(1, -3, 2)
print(answer)
