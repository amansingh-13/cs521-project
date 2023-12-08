#include <stdio.h>
int main() {    

    int number1, number2;
    
    printf("Enter an integer: ");
    scanf("%d", &number1);

    number2 = number1 + 1;
    
    // an assert statement that number 2 is always greater than number 1
    assert(number2 > number1);
}
