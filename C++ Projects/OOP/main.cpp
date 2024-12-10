#include <iostream>
#include <tuple>
using namespace std;

// concatenating tuples

int main() {
    // tuple <int, string> person(1, "John Doe");
    // cout << get<1>(person) << endl;
    // get<1>(person) = "Jane Doe";
    // cout << get<1>(person) << endl;

    // tuple <int, char, bool, float> values;
    // values = make_tuple(1, 'a', true, 3.14);
    // cout << get<1>(values) << endl;
    // cout << get<3>(values) << endl;

    // tuple <int, int> numbers1(1, 2);
    // tuple <int, int> numbers2(3, 4);
    // cout << get<0>(numbers1) << endl;
    // cout << get<1>(numbers1) << endl;
    // cout << get<0>(numbers2) << endl;
    // cout << get<1>(numbers2) << endl;
    // numbers1.swap(numbers2);
    // cout << get<0>(numbers1) << endl;
    // cout << get<1>(numbers1) << endl;
    // cout << get<0>(numbers2) << endl;
    // cout << get<1>(numbers2) << endl;

    // tuple <int, int> numbers(1, 2);
    // int x, y;
    // tie(x, y) = numbers;
    // cout << x << endl;
    // cout << y << endl;

    tuple <int, char> values1(1, 'a');
    tuple <string, bool> values2("hello", true);
    // tuple <int, char, string, bool> values3;
    // values3 = make_tuple(get<0>(values1), get<1>(values1), get<0>(values2), get<1>(values2));
    // tuple <int, char, string, bool> values3 = tuple_cat(values1, values2);
    auto values3 = tuple_cat(values1, values2);
    cout << get<0>(values3) << endl;
    cout << get<1>(values3) << endl;
    cout << get<2>(values3) << endl;
    cout << get<3>(values3) << endl;

    return 0;
}