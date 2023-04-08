# 자물쇠와 열쇠
def insert(key, lock, start_i, start_j, end):
    lenght = (2*len(key))+len(lock)-2  # 행렬 백터의 길이
    background = [[0 for i in range(lenght)]
                  for j in range(lenght)]  # 만들어진 행렬백터

    for i in range(len(key)):  # key를 먼저 background에 넣는다.
        for j in range(len(key)):
            background[start_i+i][start_j+j] = key[i][j]

    for i in range(len(key)-1, end):  # 그리고 Lock를 key가 넣어진 background에 더해준다.
        for j in range(len(key)-1, end):
            background[i][j] += lock[i-len(key)+1][j-len(key)+1]
            if background[i][j] != 1:  # 만약 1이 아닌 경우가 있다면 False 리턴
                return False

    return True


def rotate(key):
    back_key = [[0]*(len(key)) for i in range(len(key))]
    reverse = len(key)-1
    for i in range(len(key)):
        for j in range(len(key)):
            back_key[j][reverse] = key[i][j]
        reverse -= 1

    return back_key


def solution(key, lock):
    end = len(key) + len(lock) - 1
    for k in range(4):
        for i in range(end):
            for j in range(end):
                start_i = i  # key 삽입 시작 위치 (Y)
                start_j = j  # key 삽입 시작 위치 (X)
                if insert(key, lock, start_i, start_j, end) == True:
                    return True
        key = rotate(key)  # Key 회전 실시
    return False
