# 제목: 하노이의탑 문제
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.09.21

count = 0


def hanoi_tower(n, fr, tmp, to):
    global count
    count += 1
    if(n == 1):
        print("원판 1: %s --> %s" % (fr, to))
    else:
        hanoi_tower(n-1, fr, to, tmp)
        print("원판 %d: %s --> %s" % (n, fr, to))
        hanoi_tower(n-1, tmp, fr, to)


n = int(input("원반의 갯수 n(자연수)를 입력하세요:"))
hanoi_tower(n, "A", "B", "C")

print(f"함수 호출 횟수: {count}")
