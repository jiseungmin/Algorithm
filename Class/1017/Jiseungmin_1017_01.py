# 제목:  별표의 의미와 리스트 내포
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.17

nums = (1,2,3,4,5,6,7,8,9)
# 별표(*): 언팩킹의 이해
# (a1,b1,*c1) = nums
# (a2,*b2,c2) = nums
# (*a3,b3,c3) = nums
# print(a1, type(a1))
# print(b1, type(b1))
# print(c1, type(c1))

# print("----"*10)
# print(a2, type(a2))
# print(b2, type(b2))
# print(c2, type(c2))

# print("----"*10)
# print(a3, type(a3))
# print(b3, type(b3))
# print(c3, type(c3))
# nums2 = (j for j in range(1,10))
# numbers = [i for i in range(1,10)]
# numbers2 = [x for x in nums if x%3 ==0]
# print(nums, type(nums))
# print(nums2, type(nums2))
# print(numbers, type(numbers))
# print(numbers2, type(numbers2))

# 튜플 리스트 자료형 변환의 이해
from itertools import permutations

count = 0
for i in permutations(range(1,5),4):
  print(i, type(i))
  x = [*i]
  print(x, type(x))







