/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

ANS : 6857
*/

#include <iostream> 
using namespace std;

int get_largest_prime_factor(long n) {

    for (int i=2; i < n; i++) {
        if (n % i == 0) {
            return get_largest_prime_factor(n / i);
        }
    }
    return n;
}

int main() { 
    cout << get_largest_prime_factor(600851475143) << endl;
    return 0;
}