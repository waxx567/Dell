#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_set>  // For storing unique elements efficiently

using namespace std;

/*
https://www.hackerrank.com/challenges/messages-order/problem?isFullScreen=true

You are given four integers: N, S, P, Q. You will use them in order to create the sequence a with the following pseudo-code.

a[0] = S (modulo 2^31)
for i = 1 to N-1
    a[i] = a[i-1]*P+Q (modulo 2^31) 

Your task is to calculate the number of distinct integers in the sequence a.

Input Format

Four space separated integers on a single line, N, S, P, and Q respectively.

Output Format

A single integer that denotes the number of distinct integers in the sequence a.

Constraints

1 <= N <= 10^8
0 <= S, P, Q <= 2^31

Sample Input

3 1 1 1

Sample Output

3

Explanation

a = [1, 2, 3]

Hence, there are 3 different integers in the sequence.
*/


int main() {
    // Read input values: N (length), S (starting value), P (multiplier), Q (increment)
    long long N, S, P, Q;
    cin >> N >> S >> P >> Q;

    // Define the modulo value as 2^31, per the problem statement
    const long long MOD = 2147483648;

    // Use an unordered_set to store unique values in the sequence
    unordered_set<long long> distinct;

    // Initialize the first element of the sequence
    long long current = S % MOD;

    // Generate the sequence and count distinct elements
    for (long long i = 0; i < N; i++) {
        // Insert the current element into the set
        distinct.insert(current);
        
        // Generate the next element using the given formula
        current = (current * P + Q) % MOD;
    }

    // Output the number of unique elements found
    cout << distinct.size() << endl;

    return 0;
}
