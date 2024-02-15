/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

/*

1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

1,2,3,2,5,_,7,2,3,_,11,_,13,_,_,2,17,_,19,_

*/
extension Array<Int> {
    mutating func removeItem(_ item : Element) {
        for (i,_item) in self.enumerated() {
            if _item == item {
                self.remove(at: i)
            }
        }
    }
}

func get_factors(for n : Int ) -> Array<Int> {
    
    if n <= 2 {
        return [n]
    }
    
    var r_array : Array<Int> = []
    for i in 2...n-1 {
        if n%i == 0 {
            r_array.append(i)
        }
    }
    return r_array
}


func simplfied_factors(upto n: Int) -> Array<Int> {
    let range = 2...n
    var return_array = Array(range)

    for n in range.reversed() {
        for fctr in get_factors(for: n) {

            if return_array.contains(fctr) {
                return_array.removeItem(fctr)
            }
        }
    }
    
    return return_array
}

let factors_till_20 = simplfied_factors(upto: 20)
var n = 20

while true {
    var all_passed = true
    for i in factors_till_20 {
        if n % i != 0 {
            all_passed = false
            n = Int(n/i) * i + i
            // print(n)
            break
        }
    }
    if all_passed {break}
}

print(n)
//232792560