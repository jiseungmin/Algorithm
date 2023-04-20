# 뒤집기
# 아 1이랑 0이랑 갯수 비교 해서 더 작은것을 뒤집으면서 진행하면 답이 나오겠다.

s = input()
cnt = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt += 1

print((cnt+1)//2)
