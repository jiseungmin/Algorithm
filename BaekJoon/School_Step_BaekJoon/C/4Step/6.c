#include <stdio.h>

int main() {
    int n, m, a, b, t, e[100];
    
    scanf("%d %d", &n, &m);
    
    // 바구니 배열에 n개 만큼의 공을 넣는다.
    for(int i=0; i<n; i++) e[i] = i+1;
    
    // m번 공을 바꾼다.
    for(int i=0; i<m; i++) {
    	// 바꿀 바구니 2개를 입력받는다.
        scanf("%d %d", &a, &b);
        
        // 바꿀 바구니 1을 t에 저장한다.
        t = e[a-1];
        
        // 바꿀 바구니 1을 바꿀 바구니 2와 바꾼다.
        e[a-1] = e[b-1];
        
        // 바꿀 바구니 2를 저장해둔 t(바구니 1)와 바꾼다.
        e[b-1] = t;
    }
    
    // 바뀐 바구니들의 순서에 맞게 공들을 출력한다.
    for(int i=0; i<n; i++) printf("%d ", e[i]);
    
    return 0;
}