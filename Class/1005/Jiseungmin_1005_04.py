# 제목: matplotlib(외부 모듈) 막대 그래프와 파이 차트 그리기
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.05

import matplotlib.pyplot as plt

X = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
Y1 = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
Y2 = [20.1, 23.1, 23.8, 25.9, 23.4, 25.1, 26.3]

Y3 = [40, 20, 10, 30]
Y3_label = ["Eating Out", "Shopping", "Groceries", "Housing"]

# 막대 그래프
# plt.bar(X,Y1)
# plt.show()

# 파이 차트
explode = [0.1, 0, 0, 0]
plt.pie(Y3, labels=Y3_label, explode=explode)
plt.show()
