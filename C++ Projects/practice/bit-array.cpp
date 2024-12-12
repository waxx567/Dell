#include <iostream>

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
    
    // Define the modulo value
    const long long MOD = 2147483648;
    
    // Initialize sequence tracking
    long long current = S % MOD;
    long long count = 1;
    
    // Use cycle tracking with a maximum search limit
    for (long long i = 1; i < N; i++) {
        long long next = (current * P + Q) % MOD;
        if (next == current) {
            break; // Cycle detected
        }
        current = next;
        count++;
    }
    
    // Output the number of unique elements found
    cout << count << endl;
    
    return 0;
}
