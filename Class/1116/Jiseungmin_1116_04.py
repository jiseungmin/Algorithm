# 제목: 최근접 쌍의 거리(1)
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.11.16

def fib(n) :
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else :
    return fib(n-1) + fib(n-2)

def fib_iter(n):
  if (n<2):return n
  last = 0
  current = 1
  for i in range(2, n+1):
    tmp = current
    current += last
    last= tmp
  return current

def fib_mat(n):
  if n < 2:
    return n
  mat = [[1,1], [1,0]]
  result = powerMat(mat, n)
  return result[0][1]

def multiplyMat(mat1, mat2):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

def powerMat(mat, n):
    if n == 1:
        return mat
    if n % 2 == 0:
        half_power = powerMat(mat, n // 2)
        return multiplyMat(half_power, half_power)
    else:
        return multiplyMat(mat, powerMat(mat, n - 1))


print('Fibonacci 순환(5) = ', fib(5))
print('Fibonacci 반복(5) = ', fib_iter(5))
print('Fibonacci 행렬(5) = ', fib_mat(5))

for i in range(11):
  print('fib 순환(%d)='%i, fib(i))
  print('fib 반복(%d)='%i, fib_iter(i))
  print('fib 행렬(%d)='%i, fib_mat(i))
