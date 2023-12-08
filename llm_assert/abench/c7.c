#include <stdio.h>
int main() {    

    int a, b, c;
    
    printf("Enter numbers: ");
    scanf("%d %d", &a, &b);

    c = (a+b)/2;
    
    // an assert statement that c is eqaul to average of a and b
    assert(c == (a+b)/2);
}
