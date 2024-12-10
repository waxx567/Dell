#include <iostream>
#include <tuple>
using namespace std;

// changing elements in tuples 

int main() {
    tuple <int, string> person(1, "John Doe");
    cout << get<1>(person) << endl;
    get<1>(person) = "Jane Doe";
    cout << get<1>(person) << endl;
    return 0;
}