#include <iostream>
#include <vector>

using namespace std;        

int main() {
    vector<int> vct(3);
    cout << "Enter numbers: " << endl;
    for(int i = 0; i < 3; i++) {
        cin >> vct[i];
    }
    cout << "The numbers are: " << endl;

    return 0;
}