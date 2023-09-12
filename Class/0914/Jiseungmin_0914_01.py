import time


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)


n = int(input("n을 입력하세요: "))
start = time.time()
fibo(n)
end = time.time()

print(end-start)
