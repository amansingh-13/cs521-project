#include <stdio.h>
int main() {    

    int number1;
    bool number2;
    
    number1 = 5;
    number2 = true;
    
    if (number1 < 0) {
        number2 = false;
    }
    // an assert statement that number2 is always true
    assert(number2);
}
