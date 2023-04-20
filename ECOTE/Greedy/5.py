# 유튜브 모험가 문제
data = list(map(int,input().split()))
data.sort()

result = 0 # 총 그룹수
cnt = 0 # 그룹인원수

for i in data:
  cnt += 1
  if(cnt>=i):
    result += 1
    cnt = 0

print(result)