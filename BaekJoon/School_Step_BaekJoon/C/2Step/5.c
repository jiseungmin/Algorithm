#include <stdio.h>

int main(void){
    int a, b; 
    scanf("%d %d",&a,&b);

    if(b<45){
        b = b+15;
        a -= 1;
        if(a<0){a = 23;}
        printf("%d %d",a,b);
    }else{
        b = b-45;
        printf("%d %d",a,b);
    }
}

