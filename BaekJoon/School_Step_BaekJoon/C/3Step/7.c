#include <stdio.h>

int main(void){
    int a,b,n;
    scanf("%d",&n);

    for(int i=1; i<=n; i++){
        scanf("%d %d",&a,&b);
        printf("Case #%d: %d",i,a+b);
    }
    return 0;
}