#include <stdio.h>

int main(void){
    int a, b ;
    int one, two, three;
    scanf("%d",&a);
    scanf("%d",&b);

    one = a*((b%100)%10);
    two = a*((b%100)/10);
    three = a*(b/100);
    
    printf("%d\n",one);
    printf("%d\n",two);
    printf("%d\n",three);
    printf("%d",one+(two*10)+three*100);
}