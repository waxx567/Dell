#include <iostream>
#include <vector>

using namespace std;        

int main() {
    vector<int> vct(3);
    cout << "Enter numbers: " << endl;
    for(int i = 0; i < 3; i++) {
        cin >> vct[i];
    }

    int a, b, c;
    a = vct[0];
    b = vct[1];
    c = vct[2];

    cout << a + b + c << endl;

    return 0;
}