#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/*
https://www.hackerrank.com/challenges/c-tutorial-functions/problem?isFullScreen=true

Functions are a bunch of statements glued together. A function is provided with zero or more arguments, and it executes the statements on it. Based on the return type, it either returns nothing (void) or something.

Input Format

Input will contain four integers -  , one per line.

Output Format

Return the greatest of the four integers.
PS: I/O will be automatically handled.

Sample Input

3
4
6
5

Sample Output

6
*/

int greatestInt(int a, int b, int c, int d);

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    cout << greatestInt(a, b, c, d);    

    return 0;
}

int greatestInt(int a, int b, int c, int d) {
    if (a >= b && a >= c && a >= d) {
        return a;
    } else if (b >= a && b >= c && b >= d) {
        return b;
    } else if (c >= a && c >= b && c >= d) {
        return c;
    } else {
        return d;
    }
}