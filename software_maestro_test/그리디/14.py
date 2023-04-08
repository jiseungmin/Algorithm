# 캠핑
cnt = 0
while (True):
    l, p, v = map(int, input().split())
    if l+p+v == 0:
        break
    res = (v//p) * l
    res += min((v % p), l)
    cnt += 1
    print("Case {}: {}".format(cnt, res))
