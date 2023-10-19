# 제목:  리스트 내포와 제너레이터 표현식
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.17

rng = range(0,10)
print("----- 리스트 내포 -------")
list_ne = [i * i for i in rng]

for index in list_ne :
  print(index)


print("---------제너레이트 표현식----------")
gen = (i * i for i in rng)

print(next(gen))
print(next(gen))
print(next(gen))

print("--- next() ---")
for index in gen:
  print(index)







