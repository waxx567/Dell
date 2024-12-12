#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

/*
https://www.hackerrank.com/challenges/vector-sort/problem?isFullScreen=true

A template parameter pack is a template parameter that accepts zero or more template arguments (non-types, types, or templates).

Create a template function named reversed_binary_value. It must take an arbitrary number of bool values as template parameters. These booleans represent binary digits in reverse order. Your function must return an integer corresponding to the binary value of the digits represented by the booleans. For example: reversed_binary_value<0,0,1>() should return 4.

Input Format

The first line contains an integer, t, the number of test cases. Each of the t subsequent lines contains a test case. A test case is described as 2 space-separated integers, x and y, respectively.

x is the value to compare against.
y represents the range to compare: 64 x y to y + 63.

Constraints

0 <= x <= 65535
0 <= y <= 1023

The number of template parameters passed to reversed_binary_value will be <= 16.

Output Format

Each line of output contains 64 binary characters (i.e., 0's and 1's). Each character represents one value in the range. The first character corresponds to the first value in the range. The last character corresponds to the last value in the range. The character is 1 if the value in the range matches X; otherwise, the character is 0.

Sample Input

2
65 1
10 0

Sample Output

0100000000000000000000000000000000000000000000000000000000000000
0000000000100000000000000000000000000000000000000000000000000000

Explanation

The second character on the first line is a 1, because the second value in the range 64..127 is 65 and x is 65.

The eleventh character on the second line is a 1, because the eleventh value in the range 0.63 is 10 and x is 10.

All other characters are zero, because the corresponding values in the range do not match z.
*/

#include <iostream>
using namespace std;


// If rest... is empty
template<bool first, bool... rest>
auto reversed_binary_value() -> typename std::enable_if<sizeof...(rest) > 0, int>::type {
    return first + (reversed_binary_value<rest...>() << 1);
}

// Recursive template function
template<bool first, bool... rest>
int reversed_binary_value() {
    return first + (reversed_binary_value<rest...>() << 1);
}

// Base case
template<>
int reversed_binary_value<>() {
    return 0;
}

// Helper function to iterate over all combinations
template<int N>
struct CheckValues {
    static void check(int x, int y) {
        CheckValues<N-1>::check(x, y);
        int val = reversed_binary_value<((N >> 5) & 1), ((N >> 4) & 1), 
                                       ((N >> 3) & 1), ((N >> 2) & 1), 
                                       ((N >> 1) & 1), (N & 1)>();
        cout << (val == x ? '1' : '0');
    }
};

// Specialization for N = 0
template<>
struct CheckValues<0> {
    static void check(int x, int y) {
        int val = reversed_binary_value<0, 0, 0, 0, 0, 0>();
        cout << (val == x ? '1' : '0');
    }
};

int main() {
    int t;
    cin >> t;

    while (t--) {
        int x, y;
        cin >> x >> y;
        CheckValues<63>::check(x, y); // Check 64 binary values
        cout << endl;
    }

    return 0;
}
