#include <stdio.h>
int main() {    

    int number1, number2, prod;
    
    printf("Enter an integer: ");
    scanf("%d", &number1);

    number2 = -number1;
    
    // an assert statement that product of number 1 and 2 is lesser than 0
    prod = number1 * number2;
    assert(prod < 0);
}
