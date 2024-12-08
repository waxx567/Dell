#include <iostream>

// struct = a user defined data type
//          can be used to create custom data types
//          can be used to create generic classes
//          can be used to create custom containers
//          a structure that groups related data together under one name
//          arrays can only contain one data type
//          structs can contain multiple data types
//          variables inside a struct are called members
//          members can be accessed using dot notation

struct student
{
    std::string name;
    double gpa;
    bool enrolled;
};


int main() {

    student student1;
    student1.name = "John Doe";
    student1.gpa = 3.5;
    student1.enrolled = true;

    std::cout << "Name: " << student1.name << std::endl;
    std::cout << "GPA: " << student1.gpa << std::endl;
    std::cout << "Enrolled: " << student1.enrolled << std::endl;

    return 0;
}