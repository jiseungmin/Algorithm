# 제목: 윤년 계산하기
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.09.26

year = 0

if __name__ == "__main__":
    year = int(input("연도를 입력하세요: "))

    if (((year % 4 == 0) and (year % 100 != 0))) or (year % 400 == 0):
        print("%d년은 윤년입니다:" % year)
    else:
        print("%d년은 윤년이 아닙니다. " % year)
