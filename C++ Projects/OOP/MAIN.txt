#include <iostream>
#include <tuple>
using namespace std;

// tuples 

int main() {
    tuple <int, string> person(1, "John Doe");
    cout << get<0>(person) << endl;
    cout << get<1>(person) << endl;
    return 0;
}