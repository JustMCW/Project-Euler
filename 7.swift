/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
ANS : 104743
*/

import Cocoa

func is_prime (for n : Int ) -> Bool {
    if n < 2 {
        return false
    } else if n != 2 && n%2 == 0 {
        return false
    }
    

    var p = 3;
    while p * p <= n {
        if n%p == 0 {
            return false
        }
        p += 2
    }


    return true
}

var prime_counter = 1 //Includes 2
var n = 1

while prime_counter != 10_001 {
    n += 2 // odd number only
    if is_prime(for: n) {
        prime_counter += 1
    }
}

print(n)
