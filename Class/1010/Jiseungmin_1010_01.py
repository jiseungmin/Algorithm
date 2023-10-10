# 제목: 리스트, 튜플, 딕셔너리의 이해
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.10

a = [1,2,3]
b,c = [10,20,30], [100,"sunmoon",3000]
d,e = (11,21,"test"), (11,22,33)
t = 101,102,103
f = {1:1, 2:[1,2],3:c, 4:[b,d]}
g = {"k1":[b,c],"k2":[f,e]}

print(f"type a: {type(a)}, a[1]: {a[1]}, type a[1]: {type(a[0])}")
print(f"type b: {type(b)}, b[2]: {b[2]}, type b[2]: {type(b[2])}")
print(f"type c: {type(c)}, c[1][3]: {c[1][3]}, type c[1][3]: {type(c[1][3])}")
print(f"type t: {type(t)}, t[2]: {t[2]}, type t[2]: {type(t[2])}")
print(f"type d: {type(d)}, d[2][2]: {d[2][2]}, type d[2][2]: {type(d[2][2])}")
print(f"type f: {type(f)}, f[2]: {f[2]}, type f[2]: {type(f[2])}")
print(f"type g: {type(g)} g[\"k2\"][0][3]:{g['k2'][0][3]}")