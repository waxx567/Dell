#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Empty vector
    vector<int> v1;  

    // Vector with 5 elements initialized to 0
    vector<int> v2(5);  

    // Vector with 5 elements initialized to 100
    vector<int> v3(5, 100);  

    // Vector initialized with a list of values
    vector<int> v4 = {1, 2, 3, 4, 5};  

    for (int x : v4) cout << x << " ";  // Output: 1 2 3 4 5
    cout << endl;

    // push_back resizes the vector as needed
    // and adds elements to the end
    vector<string> names;
    names.push_back("Alice");
    names.push_back("Bob");
    names.push_back("Charlie");

    for (string name : names) cout << name << " "; // Output: Alice Bob Charlie
    cout << endl;

    // pop_back resizes the vector as needed
    // and removes the last element
    vector<int> numbers = {10, 20, 30};
    numbers.pop_back();  // Removes 30

    for (int num : numbers) cout << num << " ";  // Output: 10 20
    cout << endl;

    // accessing elements
    // using indexing
    cout << numbers[0] << endl; // Access the first element (10)
    // using bounds checking
    cout << numbers.at(1) << endl;  // Output: 20
    // accessing first and last element
    cout << "First: " << numbers.front() << endl;  // Output: 10
    cout << "Last: " << numbers.back() << endl;   // Output: 20

    // insert elements at a specific position
    vector<int> nums = {1, 2, 4};
    nums.insert(nums.begin() + 2, 3);  // Insert 3 at index 2

    for (int num : nums) cout << num << " "; // Output: 1 2 3 4
    cout << endl;

    // erasing elements
    vector<int> nums1 = {1, 2, 3, 4, 5};
    nums1.erase(nums1.begin() + 1);  // Remove element at index 1 (2)

    for (int num : nums1) cout << num << " "; // Output: 1 3 4 5
    cout << endl;

    return 0;
}
