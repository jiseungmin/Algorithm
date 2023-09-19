# 제목: 리스트 중복 항목 탐색
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.09.19

def unique_elements(A):
    n = len(A)
    for i in range(n-1):
        for j in range(i+1, n):
            if A[i] == A[j]:
                return False, (i+1)*(j+1)
    return True, (i+1)*(j+1)


A = [32, 14, 5, 17, 23, 9, 11, 14, 26, 29]
B = [13, 6, 8, 7, 12, 25]

print(A, unique_elements(A)[0], f"비교 횟수: {unique_elements(A)[1]}")
print(B, unique_elements(B)[0], f"비교 횟수: {unique_elements(B)[1]}")
