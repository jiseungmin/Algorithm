ddz=s = input()
count = 0

for i in range(len(s)):
    if s[i] == 'c' and s[i+1] =='=':
        count +=1
    elif s[i] == 'c' and s[i+1] =='-':
        count +=1
    elif s[i] == 'd' and s[i+1] =='z' and s[i+2] =='=':
        count +=1
    elif s[i] == 'd' and s[i+1] =='-':
        count +=1
    elif s[i] == 'l' and s[i+1] =='j':
        count +=1
    elif s[i] == 'n' and s[i+1] =='j':
        count +=1
    elif s[i] == 's' and s[i+1] =='=':
        count +=1
    elif s[i] == 'z' and s[i+1] =='=':
        count +=1
    else:
        count += 0
print(count)
print(len(s)-count/2)
    
    
    
        