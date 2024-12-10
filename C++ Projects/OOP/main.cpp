#include <iostream>
#include <tuple>
using namespace std;

// what you get if you declare but don't initialize

int main() {
    tuple <int, string> person(1, "John Doe");
    cout << get<1>(person) << endl;
    get<1>(person) = "Jane Doe";
    cout << get<1>(person) << endl;

    tuple <int, char, bool, float> values;
    // values = make_tuple(1, 'a', true, 3.14);
    cout << get<0>(values) << endl;
    cout << get<1>(values) << endl;
    cout << get<2>(values) << endl;
    cout << get<3>(values) << endl;

    return 0;
}