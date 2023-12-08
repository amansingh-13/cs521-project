#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int num1, num2;

    num1 = -2000;
    
    if (num1 > 0) {
    	num2 = 10;
    } else {
    	num2 = -10;
    }
    // an assert statment that num2 is -10
    assert(num2 == -10);
}
