#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/*
https://www.hackerrank.com/challenges/variable-sized-arrays/problem?isFullScreen=true

Consider an n-element array, a, where each index i in the array contains a reference to an array of k^i integers (where the value of k^i varies from array to array). See the Explanation section below for a diagram.

Given a, you must answer q queries. Each query is in the format i j, where i denotes an index in array a and j denotes an index in the array located at a[i]. For each query, find and print the value of element j in the array at location a[i] on a new line.

Input Format

The first line contains two space-separated integers denoting the respective values of n (the number of variable-length arrays) and q (the number of queries).
Each line i of the n subsequent lines contains a space-separated sequence in the format k a[i]^0 a[i]^1 … a[i]^k-1 describing the k-element array located at a[i].
Each of the q subsequent lines contains two space-separated integers describing the respective values of i (an index in array a) and j (an index in the array referenced by a[i]) for a query.

All indices in this challenge are zero-based.
All the given numbers are non negative and are not greater than 10^6

Output Format

For each pair of i and j values (i.e., for each query), print a single integer that denotes the element located at index j of the array referenced by a[i]. There should be a total of q lines of output.

Sample Input

2 2
3 1 5 4
5 1 2 8 9 3
0 1
1 3

Sample Output

5
9

We perform the following q = 2 queries:

1.  Find the array located at index i = 0, which corresponds to a[0] = [1,5,4]. We must print the value at index j = 1 of this array which, as you can see, is 5.
2.  Find the array located at index i = 1, which corresponds to a[1] = [1,2,8,9,3]. We must print the value at index j = 3 of this array which, as you can see, is 9.
*/

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n, q;
    cin >> n >> q;

    vector<vector<int>> a(n);

    for (int i = 0; i < n; i++) { 
        int k, x;
        cin >> k;
        for (int j = 0; j < k; j++) {
            cin >> x;
            a[i].push_back(x);
        }
    }

    for (int i = 0; i < q; i++) {
        int x, y;
        cin >> x >> y;
        cout << a[x][y] << endl;
    }

    return 0;
}
