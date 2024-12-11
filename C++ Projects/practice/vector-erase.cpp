#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/*
https://www.hackerrank.com/challenges/vector-erase/problem?isFullScreen=true

You are provided with a vector of N integers. Then, you are given  queries. For the first query, you are provided with  integer, which denotes a position in the vector. The value at this position in the vector needs to be erased. The next query consists of  integers denoting a range of the positions in the vector. The elements which fall under that range should be removed. The second query is performed on the updated vector which we get after performing the first query.

Input Format

The first line of the input contains an integer N. The next line contains N space separated integers(1-based index).The third line contains a single integer x, denoting the position of an element that should be removed from the vector. The fourth line contains two integers a and b denoting the range that should be erased from the vector inclusive of a and exclusive of b.

Output Format

Print the size of the vector in the first line and the elements of the vector after the two erase operations in the second line separated by space.

Sample Input

6
1 4 6 2 8 9
2
2 4

Sample Output

3
1 8 9
*/
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int N, x, a, b;
    cin >> N;

    vector<int> v(N);

    for (int i = 0; i < N; i++) {
        cin >> v[i];
    }

    cin >> x;
    v.erase(v.begin() + x - 1);

    cin >> a >> b;
    v.erase(v.begin() + a - 1, v.begin() + b - 1);

    cout << v.size() << endl;

    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }

    return 0;
}
