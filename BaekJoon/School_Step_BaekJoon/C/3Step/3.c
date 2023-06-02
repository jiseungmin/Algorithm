#include <stdio.h>

int main(void){
    int a ;
    int res=0;
    scanf("%d",&a);
    for(int i=1; i<=a; i++){
        res=res+i;
    }
    printf("%d",res);
}