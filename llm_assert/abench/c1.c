#include <stdio.h>
int main() {    

    int number1, number2, sum;
    
    printf("Enter two integers: ");
    scanf("%d %d", &number1, &number2);

    number2 = -number1;
    
    // an assert statement that sum of number 1 and 2 is 0
    sum = number1 + number2;
    assert(sum == 0);
}
