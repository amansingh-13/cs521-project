#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int num1, sum = 0;

    num1 = 10;
    
    while(1) {
    	if(num1 > 0) {
    	    sum = sum + 1;
    	} else {
    	    break;
    	}
    	num1 = num1 - 1;
    }
    // an assert statement that sum equals the initial value of num1
    assert(sum == 10);
}
