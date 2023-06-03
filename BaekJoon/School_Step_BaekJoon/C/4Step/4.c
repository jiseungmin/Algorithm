#include <stdio.h>

int main(){
	int index=1;
	int arr[9];
	
	for(int i=0; i<sizeof(arr)/sizeof(arr[0]); i++){
		scanf("%d", &arr[i]);
	}

	int max = arr[0];
	for(int i=0; i<sizeof(arr)/sizeof(arr[0]); i++){
		if(arr[i]>max) {
			max = arr[i];
			index = i+1;
		}
	}
	printf("%d\n", max);
    printf("%d", index);

	return 0;
}