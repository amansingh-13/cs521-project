#include <stdio.h>

int main(){
	int N;
	scanf("%d", &N);
	printf("Sum of 1 to %d is %d\n", N, N*(N+1)/2);
	
	// assert statement that checks sum of 1 to N is N*(N+1)/2 by adding the numbers in a for loop
	int sum = 0;
	for(int i = 1; i <= N; i++){
		sum += i;
	}
	assert(sum == N*(N+1)/2);
}
