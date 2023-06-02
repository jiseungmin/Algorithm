#include <stdio.h>

int main(void){
    int a, b, c; 
    scanf("%d %d",&a,&b);
    scanf("%d",&c);
    if(b+c>=60){
        a += (b+c) / 60;
        if(a>=24){
            a -= 24;
        }
        b = (b+c)%60;
        printf("%d %d",a,b);
    } else{
        b += c;
        printf("%d %d",a,b);
    }
    
    return 0;
}

