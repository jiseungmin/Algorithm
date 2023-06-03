#include <stdio.h>

int main(){
    int a,n,b, count=0;
    int ar[100];
    scanf("%d",&a);

    for(int i=0; i<a; i++){
        scanf("%d",&n);
        ar[i] = n;
    }
    
    scanf("%d",&b);
    for(int i=0; i<a; i++){
        if(ar[i]==b){
            count+=1;
        }
    }

    printf("%d",count);
    return 0;
}