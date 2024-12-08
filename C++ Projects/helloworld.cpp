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


// you can also set a default value on members
struct student
{
    std::string name;
    double gpa;
    bool enrolled = true;
};

int main() {

    student student1;
    student1.name = "John Doe";
    student1.gpa = 3.5;

    student student2;
    student2.name = "Jane Doe";
    student2.gpa = 4.0;

    student student3;
    student3.name = "Joe Doe";
    student3.gpa = 2.8;

    std::cout << "Name: " << student1.name << std::endl;
    std::cout << "GPA: " << student1.gpa << std::endl;
    std::cout << "Enrolled: " << student1.enrolled << std::endl;

    std::cout << "Name: " << student2.name << std::endl;
    std::cout << "GPA: " << student2.gpa << std::endl;
    std::cout << "Enrolled: " << student2.enrolled << std::endl;

    std::cout << "Name: " << student3.name << std::endl;
    std::cout << "GPA: " << student3.gpa << std::endl;
    std::cout << "Enrolled: " << student3.enrolled << std::endl;

    return 0;
}