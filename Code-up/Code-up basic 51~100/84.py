from posixpath import split


h,b,c,s =map(int,input().split())

print(str(round(h*b*c*s/8/1024/1024,1))+" MB")