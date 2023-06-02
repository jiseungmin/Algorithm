#include <stdio.h>

int main(void) {
    int res;
    int a;
    int check = 0; 
    scanf("%d %d", &res, &a);

    for (int i = 0; i < a; i++) {
        int price = 0, mul = 0;
        scanf("%d %d", &price, &mul);
        check += price * mul;
    }

    if (res == check) {
        printf("Yes\n");
    } else {
        printf("No\n");  
    }

    return 0; 
}