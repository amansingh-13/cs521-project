#include <stdio.h>

int main() {
    char* s1 = "hello";
    char* s2 = "world";
    
    int num = 0;
    
    while(1) {
    	if(num > 10) {
    	    s1 = "world";
    	    break;
    	} else {
    	    num++;
    	}
    }
    
    // an assert statement that string s1 and s2 have the same content
    assert(strcmp(s1,s2) == 0);
}
