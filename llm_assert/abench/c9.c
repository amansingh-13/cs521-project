#include <stdio.h>
int main() {    

    int number1, number2;
    
    number1 = 5;
    number2 = number1 + 1;
    
    // an assert statement that sum of number 1 and 2 is odd
    int sum = number1 + number2;
    assert(sum % 2 == 1);
}
