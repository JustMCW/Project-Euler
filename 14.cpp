/*
he following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

#include <iostream>

using namespace std;

int get_steps (int number)
{
	long long n = number;
	int counter = 0;

	
	return counter;
}

int main ()
{
	int largest_step = 0;
	int largest_num = 0;

	for (int i=1;i < 1000000;i++) {
		int steps = 0;
		long x = i; //Long is required or it'll overflow

		while (x != 1) {
			if (x % 2 == 1) {
				x = 3*x + 1;
			} else {
				x /= 2;
			}
			steps += 1;
		}

		if (steps > largest_step) {
			largest_step = steps;
			largest_num = i;
		}
	}
	
	cout << largest_num << " with " << largest_step << " steps." << endl;
	return 0;
}
