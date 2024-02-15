

import Foundation

let num = 2_000_000
var prime = Array(repeating: true, count: num+1)
var p = 2

var sum = 0
let t = CFAbsoluteTimeGetCurrent()
while (p * p <= num) {
    if (prime[p] == true) {
        for i in stride(from: p*p, to: num+1, by: p) {
            prime[i] = false
        }
    }
    p += 1
}
//Print all prime numbers
for p in 2...num {
    if prime[p] {
        sum += p
    }
}
var d = CFAbsoluteTimeGetCurrent() - t
print(sum,d)
