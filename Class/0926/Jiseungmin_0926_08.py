# 제목: 리스트와 튜플의 차이와 이해
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.09.26

def sunmmon():
    return(11, 12, 13, 14)


aaa = sunmmon()
print(sunmmon(), type(sunmmon()))
print(aaa[0], type[aaa[0]])

[a, b] = [10, 20]
(c, d) = (10, 20)
e = [100, 200, 300, 400]
f = 101, 201, 301, 401
a, b = b, a

print("a:", a, 'type=', type(a))
print("b:", b, 'type=', type(b))
print("c:", c, 'type=', type(c))
print("d:", d, 'type=', type(d))
print("e:", e, 'type=', type(e))
print("f:", f, 'type=', type(f))

print(e[1])
print(f[1])
