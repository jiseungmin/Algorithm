# 제목: 세트와 딕셔너리의 차이
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.17

A = {1,"선문", "아산", "탕정",5,"아산",5}
B = [1,"선문", "아산", "탕정",5, "아산", 5]
C = {1:1, "선문":"sunmoon", "아산":"Asan", 5:5}

print(A, type(A))
print(B, type(B))
print(C, type(C))
print(C["선문"])
print(B[1])
# print(A[1])






