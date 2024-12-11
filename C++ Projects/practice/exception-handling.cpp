#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/*
https://www.hackerrank.com/challenges/vector-sort/problem?isFullScreen=true

In this challenge, the task is to debug the existing code to successfully execute all provided test files.

You are required to extend the existing code so that it handles std::invalid_argument exception properly. 

Input Format

The input is read by the provided locked code template. In the only line of the input, there is a single integer n, which is going to be the argument passed to function process_input.

Output Format

The output should be produced by function process_input as described in the statement.

Sample Input 0

0

Sample Output 0

largest proper divisor is not defined for n=0
returning control flow to caller
Sample Input 1

9

Sample Output 1

result=3
returning control flow to caller
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stdexcept>
using namespace std;

int largest_proper_divisor(int n) {
    if (n == 0) {
        throw invalid_argument("largest proper divisor is not defined for n=0");
    }
    if (n == 1) {
        throw invalid_argument("largest proper divisor is not defined for n=1");
    }
    for (int i = n / 2; i >= 1; --i) {
        if (n % i == 0) {
            return i;
        }
    }
    return -1; 
}

void process_input(int n) {
    try {
        int result = largest_proper_divisor(n);
        cout << "result=" << result << endl;
    } catch (invalid_argument &e) {
        cout << e.what() << endl;
    }
    cout << "returning control flow to caller" << endl;
}

int main() {
    int n;
    cin >> n;
    process_input(n);
    return 0;
}
