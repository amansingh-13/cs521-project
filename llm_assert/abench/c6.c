#include <stdio.h>
int main() {    

    int number1;
    int number2;
    
    number1 = 5;
    number2 = 0;
    
    if (number1 < 0) {
        number2 = number2 + 1;
    }
    // an assert statement that number2 is 0
    assert(number2 == 0);
}
