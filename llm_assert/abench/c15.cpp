#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int num1, sum = 0;

    num1 = 10;
    
    for(int i=1;i<=num1;i++) {
    	sum = sum + i;
    }
    // an assert statement that sum equals the sum of first 10 consecutive positive integers
    assert(sum == (num1+1)*num1/2);
}
