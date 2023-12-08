#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int num1, num2;

    cout << "Enter first number: ";
    cin >> num1;

    cout << "Enter second number: ";
    cin >> num2;

    int maxNumber = max(num1, num2);

    // an assert statement that maxNumber is not greater than num1 and num2
    assert(maxNumber <= num1 || maxNumber <= num2);
}
