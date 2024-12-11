#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Empty vector
    vector<int> v1;  

    // Vector with 5 elements initialized to 0
    vector<int> v2(5);  

    // Vector with 5 elements initialized to 100
    vector<int> v3(5, 100);  

    // Vector initialized with a list of values
    vector<int> v4 = {1, 2, 3, 4, 5};  

    for (int x : v4) cout << x << " ";

    return 0;
}
