/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

ANS : 
*/

#include <iostream> 
using namespace std;

bool is_palindrome(int n) {
    string str = to_string(n);
    for (int i=0; i < str.length()/2 ; i++) {
        if (str[i] != str[str.length() - 1 - i]) {
            return false;
        }
    }
    return true;
}

int main() { 
    int max = 0;
    for (int i=100;i < 1000; i++) {
        for (int j=100;j < 1000; j++) {
            const int r = i*j;
            if (is_palindrome(r) && r > max) {
                max = r;
            }
        }
    }
    cout<<max<<endl;
    return 0;
}