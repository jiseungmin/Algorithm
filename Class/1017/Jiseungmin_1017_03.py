# 제목: try except로 예외처리하기
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.17

try:
  num_a = int(input("반지름 입력(정수):"))
except:
  print("정수로 정확하게 입력하세요.")
else:
    print("원의 반지름", num_a)
    print("원의 둘레", 2*3.14*num_a)
    print("원의 넓이", 3.14*num_a*num_a)
finally:
   print("프로그램이 종료되었습니다.")








