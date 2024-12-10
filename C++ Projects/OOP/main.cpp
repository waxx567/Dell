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

    tuple <int, int> numbers(1, 2);
    cout << get<0>(numbers) << endl;
    cout << get<1>(numbers) << endl;
    swap(get<0>(numbers), get<1>(numbers));
    cout << get<0>(numbers) << endl;
    cout << get<1>(numbers) << endl;

    return 0;
}