#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    string s1 = "hello";
    string s2 = "world";
    string s3 = s1 + s2;
    
    // an assert statement that length of string 3 is sum of lengths of string 1 and string 2
    assert(s3.length() == s1.length() + s2.length());
}
