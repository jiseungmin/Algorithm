#include <stdio.h>

int main(void){
    int a,b, n;
    int ar[10000];
    scanf("%d %d", &a,&b);

    for(int i =0; i<a; i++){
        scanf("%d",&n);
        ar[i] = n;
    }
    
    for(int i =0; i<a; i++){
     if(ar[i]<b){
            printf("%d",ar[i]);
        }
    }

    return 0;
}