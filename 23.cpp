#include <iostream>
#include <vector>
#include <set>

using namespace std;

bool is_abundant(int x) {
    int p = 2;
    int s = 1;
    while (p*p <= x) {
        if (x%p == 0) {
            s += p;
            int p2 = x/p;
            if (p != p2){
                s += p2;
            }
        }
        p += 1;
    }
    return x < s;
}

int main() {
    int sum = 0;
    vector<int> abundant_numbers;
    set<int> can_be_expressed;

    const int limit = 28123;

    for (int i =1; i <= 28123; i++) {
        sum += i;
        if (is_abundant(i)) {
            abundant_numbers.push_back(i);
            for (int n : abundant_numbers) {
                int add_up = i+n;
                if (add_up < 0) {
                    cout << i << " " << n << endl;
                }
                if (add_up <= 28123) {
                    sum -= add_up;
                    can_be_expressed.insert(add_up);
                }
            }
        }
    }

    // for (int not_valid : can_be_expressed) {
    //     sum -= not_valid;
    // }

    //35_213_988
    //395,465,626 for sum of 1 to 28123
    //430,679,614

    cout << sum << endl; // 4_179_871
    return 0;
}