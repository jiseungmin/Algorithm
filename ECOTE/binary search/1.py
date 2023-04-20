# 떡볶이 떡 만들기

# 떡 개수와 요청한 떡의 길이를 입력받기
n, m = map(int, input().split())
# 각 떡의 개별 높이 정보를 입력받기
a = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(a)

result = 0
while(start <= end):
    total = 0
    mid = (start+end) // 2

    for x in a:
        # 잘렸을 때의 떡의 양 계산
        if x > mid:
            total += x-mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid-1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid
        start = mid+1

print(result)
