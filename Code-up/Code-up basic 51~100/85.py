from tokenize import Double


h,b,s =map(int,input().split())
s = s/8/1024/1024  
print("{:.2f}".format(h*b*s),"MB",end=' ') 
   

