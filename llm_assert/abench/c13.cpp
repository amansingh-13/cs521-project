#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int num1, num2;

    num1 = -2000;
    num2 = abs(num1);


    // an assert statement that num2 is equal to the absolute value of num1
    assert(num2 == -num1);
}
