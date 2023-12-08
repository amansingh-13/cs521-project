#include <stdio.h>

#define LIST_LEN 20

int abs(int x){
	return x > 0 ? x : -x;
}

int main(){
	int arr[LIST_LEN];

	for(int i = 0; i < LIST_LEN; i++){
		int inp;
		scanf("%d", &inp);
		arr[i] = abs(inp);
	}
	
	// assert statements that all elements of arr are greater than equal 0
	for(int i = 0; i < LIST_LEN; i++){
		assert(arr[i] >= 0);
	}
}
