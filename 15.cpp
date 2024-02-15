/*
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
*/

#include <iostream>

using namespace std;

long long path_count;

void walk_path (int size, int x, int y) {
    if (x == size && y == size) { // Reached the end
        path_count++;
    } else { // Either goes down or right, and become closer to the destination.
        if (x < size) {
            walk_path(size, x+1,y);
        };
        if (y < size) {
            walk_path(size, x,y+1);
        };
    };
}


int main () {
    walk_path(20,0,0);
    cout << path_count << endl;
    return 0;
}


/*
0 : 1 1/0
1 : 2 2/1
2 : 6 3/1
3 : 20 10/3
4 : 70 7/2
5 : 252 18/5
6 : 924 11/3
7 : 3432 26/7
8 : 12870 15/4
9 : 48620 34/9
10 : 184756 19/5
11 : 705432 42/11
12 : 2704156 23/6
13 : 10400600 50/13
14 : 40116600 27/7
15 : 155117520 58/15
16 : 601080390 31/8
17 : -1961361076 -980680538/300540195
18 : 485200708 485200708/-196136107
*/