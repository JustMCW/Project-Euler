/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/

import Cocoa

func is_interger(for x : Double) -> Bool {
    return x.rounded() == x
}

func main () {
    for i in 1...999 {
        for j in 1...999 {
            
            if i + j >= 1000 { continue }
            if !is_interger(for: sqrt(Double(i*i + j*j)) ) { continue }
            
            for k in 1...999 {
                if k > i && k > j {
                    if i + j + k == 1000 {
                        if i*i + j*j == k*k {
                            print(i,j,k) //200 375 425 , yes go
                            print(i*j*k)
                            return
                        }
                    }
                }
            }
        }
    }

}

main()

