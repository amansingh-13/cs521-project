#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int num1, num2;

    num1 = 2000;
    num2 = 100;

    int quotient = num1/num2;

    // assert statement that dividend is divisible by divisor
    assert(num1 % num2 == 0);
}
