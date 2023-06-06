#include <stdio.h>

int main(void) {
    int a;
    double arr[1000];
    scanf("%d", &a);

    for (int i = 0; i < a; i++) {
        scanf("%lf", &arr[i]);  
    }
    
    double max = arr[0];  
    for (int i = 0; i < a; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    
    double sum = 0;
    for (int i = 0; i < a; i++) {
        arr[i] = arr[i] / max * 100.0;
        sum += arr[i];
    }

    printf("%.2lf", sum / a);  

    return 0;
}
