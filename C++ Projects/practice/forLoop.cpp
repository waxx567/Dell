#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

/*
https://www.hackerrank.com/challenges/c-tutorial-for-loop/problem?isFullScreen=true

Input Format

You will be given two positive integers, a and b (a <= b), separated by a newline.

Output Format

For each integer n in the inclusive interval [a, b]:

    - If 1 <= n <= 9, then print the English representation of it in lowercase. That is "one" for 1, "two" for 2, and so on.
    - Else if n > 9 and it is an even number, then print "even".
    - Else if n > 9 and it is an odd number, then print "odd".

Sample Input

8
11

Sample Output

eight
nine
even
odd

*/

using namespace std;

void NumbersToWords(int a, int b);

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */

    int a, b;
    cin >> a >> b;

    NumbersToWords(a, b);

    return 0;
}

void NumbersToWords(int a, int b) {
    for (int i = a; i <= b; i++) {
        if (i >= 1 && i <= 9) {
            if (i == 1) {
                cout << "one" << endl;
            } else if (i == 2) {
                cout << "two" << endl;
            } else if (i == 3) {
                cout << "three" << endl;
            } else if (i == 4) {
                cout << "four" << endl;
            } else if (i == 5) {
                cout << "five" << endl;
            } else if (i == 6) {
                cout << "six" << endl;
            } else if (i == 7) {
                cout << "seven" << endl;
            } else if (i == 8) {
                cout << "eight" << endl;
            } else if (i == 9) {
                cout << "nine" << endl;
            }
        } else if (i > 9 && i % 2 == 0) {
            cout << "even" << endl;
        } else if (i > 9 && i % 2 != 0) {
            cout << "odd" << endl;
        }
    }
}