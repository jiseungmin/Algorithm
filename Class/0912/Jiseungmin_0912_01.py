# 제목 : 최대닶 찾기
# 이름 : 지승민
# 날짜 : 2023.09.12

def find_max(a):
    max = a[0]
    for i in range(len(a)):
        if max < a[i]:
            max = a[i]
    return max


array = [20, 34, 12, 92, 84, 39, 64, 55, 24]
print(array, "최대값=", find_max(array))
