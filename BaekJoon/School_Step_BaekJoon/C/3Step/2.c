#include <stdio.h>

int main(void){
    int a,b,c;
    scanf("%d", &a);
    for(int i=0; i<a; i++){
        printf("%d * %d = %d\n",a,i,a*i);
    }
}