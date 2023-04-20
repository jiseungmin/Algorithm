# 부품 찾기
n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))


def binary_search(array, start, end, target):
    if start > end:
        return None

    mid = (start+end) // 2

    if array[mid] == target:
        return True

    elif array[mid] > target:
        return binary_search(array, start, mid-1, target)

    else:
        return binary_search(array, mid+1, end, target)


for i in range(m):
    if binary_search(a, 0, n-1, b[i]) == True:
        print("yes", end=" ")
    else:
        print("no", end=" ")
