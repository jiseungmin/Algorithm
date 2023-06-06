#include <stdio.h>

int main()
{
	int n, input, min = 1000000, max = -1000000; // 최대값, 최소값 설정 주의

	scanf("%d", &n);

	for (int i = 0; i < n; i++) { // n개의 정수만큼 최소, 최대 비교
		scanf("%d", &input);

		if (input >= max) {
			max = input;
		}

		if (input <= min) {
			min = input;
		}
	}

	printf("%d %d", min, max);

	return 0;
}