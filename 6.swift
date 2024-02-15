/*
The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2+...+ 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1+2+...+10)^2= 55^2 =3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/

import Cocoa

let n = 100

var sum_of_sqaures = 0
var sqaure_of_sum = 0

for i in 1...n {
    sum_of_sqaures += i * i
    sqaure_of_sum += i
}
sqaure_of_sum = sqaure_of_sum * sqaure_of_sum

print(sqaure_of_sum-sum_of_sqaures)
