#include <iostream>
using namespace std;

class Employee {
public:
    string Name;
    string Company;
    int Age;
};
int main() {
    Employee employee1;
    employee1.Name = "John Doe";
    employee1.Company = "ABC Company";
    employee1.Age = 30;
    cout << employee1.Name << endl;
    cout << employee1.Company << endl;
    cout << employee1.Age << endl;
    return 0;
}