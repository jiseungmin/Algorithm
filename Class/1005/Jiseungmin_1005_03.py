# 제목: 인라인 람다 - 함수의 매개변수(인수)로 바로 사용
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.05

list_input_a = [1, 2, 3, 4, 5]

output_a = map(lambda x: x*x*x, list_input_a)
print(list(output_a))

output_b = filter(lambda x: x < 4, list_input_a)
print(list(output_b))
