#include <iostream>
#include <map>
using namespace std;

// maps 

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
    cout << scores["John"] << endl;
    cout << scores["Jane"] << endl;
    cout << scores["Jack"] << endl;
    cout << scores["Jill"] << endl;

    return 0;
}