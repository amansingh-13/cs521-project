#include <stdio.h>
int main() {    

    int a, b, c;
    
    printf("Enter numbers: ");
    scanf("%d %d", &a, &b);

    c = a+b;
    
    // an assert statement that c is eqaul to sum of a and b
    assert(c == a+b);
}
