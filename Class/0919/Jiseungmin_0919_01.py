# 제목: 순차 탐색의 효율성 계산
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.09.19

a = [32, 14, 5, 17, 23, 9, 11, 4, 26, 29]


def seq_search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1


key = int(input("찾고자 하는 Key 번호를 입력하세여: "))
count = seq_search(a, key)

print(f"리스트 a의 크기: {len(a)} 비교횟수: {count+1}")
