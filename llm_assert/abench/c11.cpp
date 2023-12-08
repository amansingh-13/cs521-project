#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int num1, num2, ans;

    cout << "Enter first number: ";
    cin >> num1;

    num2 = -1;
    
    for(int i=0; i<10;i++) {
        ans = num1*num2;
    }

    // an assert statement that ans is equal to num1
    assert(ans == num1);
}
