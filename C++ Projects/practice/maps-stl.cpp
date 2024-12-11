#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

/*
https://www.hackerrank.com/challenges/vector-sort/problem?isFullScreen=true

Maps are a part of the C++ STL.Maps are associative containers that store elements formed by a combination of a key value and a mapped value, following a specific order.

Input Format

The first line of the input contains Q where Q is the number of queries. The next Q lines contain 1 query each.The first integer, `type` of each query is the type of the query. If query is of type 1, it consists of one string and an integer X and Y where X is the name of the student and Y is the marks of the student. If query is of type 2 or 3,it consists of a single string X where X is the name of the student.

Output Format

For queries of type 3 print the marks of the given student.

Sample Input

7
1 Jesse 20
1 Jess 12
1 Jess 18
3 Jess
3 Jesse
2 Jess
3 Jess

Sample Output

30
20
0
*/

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int Q, type, Y;
    string X;
    cin >> Q;

    map<string, int> m;

    for (int i = 0; i < Q; i++) {
        cin >> type >> X;
        if (type == 1) {
            cin >> Y;
            m[X] += Y;
        } else if (type == 2) {
            m.erase(X);
        } else if (type == 3) {
            map<string, int>::iterator it = m.find(X);

            if (it != m.end()) {
                cout << it->second << endl;
            } else {
                cout << 0 << endl;
            }
        }
    }
    
    return 0;
}
