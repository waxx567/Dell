#include <iostream>
using namespace std;

class Employee {
public:
    string Name;
    string Company;
    int Age;

    void print() {
        cout << "Name: " << Name << endl;
        cout << "Company: " << Company << endl;
        cout << "Age: " << Age << endl;
    }
};
int main() {
    Employee employee1;
    employee1.Name = "John Doe";
    employee1.Company = "ABC Company";
    employee1.Age = 30;

    employee1.print();
    
    return 0;
}