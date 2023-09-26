# 제목: 문자열과 리스트의 인데스 이해
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.09.26

univ = "선문대학교"
test = "동해물과 백두산이 마르고 닳도록"
line = test.split(" ")

print(univ, "type: ", type(univ))
print(univ[0], "type: ", type(univ[0]))
print(univ[0:3], "type: ", type(univ[0:3]))
print(univ[-1], "type: ", type(univ[-1]))

print(line[0], "type: ", type(line[0]))

print(line, "type: ", type(line))
