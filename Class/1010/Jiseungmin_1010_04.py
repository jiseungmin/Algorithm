# 제목:  문자열 매칭 with python
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.10

def stringmatching(T,P):
  n = len(T)
  m = len(P)
  for i in range(n-m+1):
    j = 0
    while j < m and P[j] == T[i+j]:
      j = j +1
    if j == m :
      return i
  return -1

text = "HELLO WORLD"
pattern = "LO"
print(pattern, 'in', text, '-->', stringmatching(text,pattern))
pattern = "HI"
print(pattern, 'in', text, '-->', stringmatching(text,pattern))