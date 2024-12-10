#include <iostream>
#include <vector>

using namespace std;        

int main() {
    vector<int> vct(3);
    cout << "Enter numbers: " << endl;
    for(int i = 0; i < 3; i++) {
        cin >> vct[i];
    }

    for(int i = 0; i < 3; i++) {
        cout << "Numbers: " << vct[i] << endl;
    }

    return 0;
}