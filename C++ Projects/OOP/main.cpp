#include <iostream>
#include <tuple>
using namespace std;

// swapping the contents of two tuples

int main() {
    // tuple <int, string> person(1, "John Doe");
    // cout << get<1>(person) << endl;
    // get<1>(person) = "Jane Doe";
    // cout << get<1>(person) << endl;

    // tuple <int, char, bool, float> values;
    // values = make_tuple(1, 'a', true, 3.14);
    // cout << get<1>(values) << endl;
    // cout << get<3>(values) << endl;

    tuple <int, int> numbers1(1, 2);
    tuple <int, int> numbers2(3, 4);
    cout << get<0>(numbers1) << endl;
    cout << get<1>(numbers1) << endl;
    cout << get<0>(numbers2) << endl;
    cout << get<1>(numbers2) << endl;
    numbers1.swap(numbers2);
    cout << get<0>(numbers1) << endl;
    cout << get<1>(numbers1) << endl;
    cout << get<0>(numbers2) << endl;
    cout << get<1>(numbers2) << endl;

    return 0;
}