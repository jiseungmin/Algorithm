# 제목:  팩토리얼 하향식·상향식 축소 정복기법
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.31

def factorial_recur(n):
  if n == 1 :
    return 1
  else :
    return n * factorial_recur(n-1)
  
def factorial_iter(n):
  result  =1
  for k in range(n,0,-1):
    result = result * k
  return result

n = int(input("정수 n을 입력하세요: "))
print(f"하향식(순환) Factorial({n})={factorial_recur(n)}")
print(f"상향식(순환) Factorial({n})={factorial_iter(n)}")
      

