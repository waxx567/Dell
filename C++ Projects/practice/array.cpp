#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/*
https://www.hackerrank.com/challenges/c-tutorial-array/problem?isFullScreen=true

An array is a series of elements of the same type placed in contiguous memory locations that can be individually referenced by adding an index to a unique identifier.

You will be given an array of N integers and you have to print the integers in the reverse order.

Input Format

The first line of the input contains ,where N is the number of integers.The next line contains N space-separated integers.

Constraints

1 <= N <= 1000
1 <= A[i] <= 1000, where A[i] is the ith integer in the array.

Output Format

Print the N integers of the array in the reverse order, space-separated on a single line.

Sample Input

4
1 4 3 2

Sample Output

2 3 4 1
*/


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int N;
    cin >> N; 
    
    vector<int> arr(N);
    
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    
    for (int i = N-1; i >= 0; i--) {
        cout << arr[i]+1 << ' ';
    }
    cout << endl;

    return 0;
}
