#include <stdio.h>

int main(void){
    char a[1000];
    int n;
    scanf("%s %d",a,&n);
    printf("%c",a[n-1]);
    return 0;
}