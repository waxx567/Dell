#include <iostream>
#include <map>
using namespace std;

// inserting map pairs 

int main() {
    // map <string, int> scores;
    // scores["John"] = 90;
    // scores["Jane"] = 80;
    // scores["Jack"] = 70;
    // scores["Jill"] = 60;
    // or
    map <string, int> scores = {
        {"John", 90},
        {"Jane", 80},
        {"Jack", 70},
        {"Jill", 60}
    };
    // prints the values of the keys
    // cout << scores["John"] << endl;
    // cout << scores["Jane"] << endl;
    // cout << scores["Jack"] << endl;
    // cout << scores["Jill"] << endl;
    scores["Jean"] = 50;
    cout << scores["Jean"] << endl;

    return 0;
}