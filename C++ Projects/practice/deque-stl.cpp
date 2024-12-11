#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <deque>
using namespace std;

/*
https://www.hackerrank.com/challenges/vector-sort/problem?isFullScreen=true

Double ended queue or Deque(part of C++ STL) are sequence containers with dynamic sizes that can be expanded or contracted on both ends (either its front or its back).

Input Format

First line of input will contain the number of test cases T. For each test case, you will be given the size of array N and the size of subarray to be used K. This will be followed by the elements of the array Ai.

Output Format

For each of the contiguous subarrays of size K of each array, you have to print the maximum integer.

Sample Input

2
5 2
3 4 6 3 4
7 4
3 4 5 8 1 4 10

Sample Output

4 6 6 4
8 8 8 10
*/

#include <iostream>
#include <vector>
#include <deque>
using namespace std;

int main() {
    int T, N, K;
    cin >> T;

    for (int i = 0; i < T; i++) {
        cin >> N >> K;

        vector<int> a(N);
        for (int j = 0; j < N; j++) {
            cin >> a[j];
        }

        deque<int> dq;

        for (int j = 0; j < N; j++) {
            // Remove elements outside the current window
            if (!dq.empty() && dq.front() == j - K) {
                dq.pop_front();
            }

            // Remove elements smaller than the current one from the back
            while (!dq.empty() && a[dq.back()] <= a[j]) {
                dq.pop_back();
            }

            // Add the current element's index
            dq.push_back(j);

            // Print maximum of current window
            if (j >= K - 1) {
                cout << a[dq.front()] << " ";
            }
        }
        cout << endl;
    }
    
    return 0;
}