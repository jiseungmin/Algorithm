# 제목 : DP로 구현한 파보나치 수열의 성능측정
# 이름 : 지승민
# 날짜 : 2023.09.14

import time
n = int(input("n을 입력하세요: "))
dictionary = {1:1,2:1}
counter = 0

def fibo(n):
    global counter
    counter += 1
    if n in dictionary :
        return dictionary[n]
    else :
        output = fibo(n-1) + fibo(n-2)
        dictionary[n] = output
        return output

start = time.time()
fibo(n)
end = time.time()

print("-------------------------------------------------")
print(f"fibo({n}) 계산에 활용된 덧셈 횟수는 {counter}번 입니다.")
print("실행시간=", end-start)