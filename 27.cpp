
#include <iostream>
#include <chrono>

using namespace std;

bool is_prime(int n) {
    if (n < 2 || n%2 == 0) {
        return false;
    };
    int p = 3;
    while (p*p < n) {
        if (n%p==0) {
            return false;
        };
        p += 2;
    };
    return true;
};

int main() {
    int max_n = 1;
    int max_product = 0;
    auto start = chrono::steady_clock::now();

    for (int scalor = -999; scalor < 1000; scalor++) {
        for (int coeffcient = 0; coeffcient < 1001; coeffcient++) {
            int n = 0;    
            for (n=0; n < coeffcient; n++) {
                int r = n * (scalor + n) + coeffcient;
                if (!is_prime(r)) {
                    break;
                } 
            }

            if (n >= max_n) {
                max_n = n;
                max_product = coeffcient * scalor;
            }
        }
    }
    auto end = chrono::steady_clock::now();
    cout << max_product << endl;
    cout << chrono::duration_cast<chrono::milliseconds>(end - start).count() << " ms" << endl;
    return 0;
};

