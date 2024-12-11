#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

/*
https://www.hackerrank.com/challenges/vector-sort/problem?isFullScreen=true

Sets are a part of the C++ STL. Sets are containers that store unique elements following a specific order. 

Input Format

The first line of the input contains Q where Q is the number of queries. The next Q lines contain 1 query each. Each query consists of two integers y and z where y is the type of the query and z is an integer.

Output Format

For queries of type 3 print "Yes"(without quotes) if the number z is present in the set and if the number is not present, then print "No"(without quotes).
Each query of type 3 should be printed in a new line.

Sample Input

8
1 9
1 6
1 10
1 4
3 6
3 14
2 6
3 6

Sample Output

Yes
No
No
*/

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int Q, y, z;
    cin >> Q;

    set <int> s;

    for (int i = 0; i < Q; i++) {
        cin >> y >> z;
        
        if (y == 1) {
            s.insert(z);
        } else if (y == 2) {
            s.erase(z);
        } else if (y == 3) {
            set<int>::iterator it = s.find(z);
            if (it != s.end()) {
                cout << "Yes" << endl;
            } else {
                cout << "No" << endl;
            }
        }
    }   

    return 0;
}
