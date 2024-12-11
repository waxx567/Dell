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

    for (int x : v4) cout << x << " ";  // Output: 1 2 3 4 5
    cout << endl;

    // push_back resizes the vector as needed
    vector<string> names;
    names.push_back("Alice");
    names.push_back("Bob");
    names.push_back("Charlie");

    for (string name : names) cout << name << " "; // Output: Alice Bob Charlie
    cout << endl;

    return 0;
}
