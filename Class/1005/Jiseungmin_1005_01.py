# 제목: BMI 지수로 비만도 판별
# 작성자 : 컴퓨터 공학부 지승민
# 작성일 : 2023.10.05

height = float(input("키를 m으로 입력하세요: "))
weight = float(input("몸무게를 kg으로 입력하세요: "))


def calcBMI(height, weight):
    bmi = weight / (height*height)
    return bmi

def checkBMI(bmi):
    if bmi > 30:
        print(f"당신의 BMI는 {bmi:.1f}이고, 비만입니다.")
    elif bmi > 25 :
        print(f"당신의 BMI는 {bmi:.1f}이고, 정상입니다.")
    elif bmi > 18 :
        print(f"당신의 BMI는 {bmi:.1f}이고, 저체중입니다.")

# 함수 호출 (실행)
result = calcBMI(height, weight)
checkBMI(result)