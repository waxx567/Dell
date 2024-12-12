#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

/*
https://www.hackerrank.com/challenges/vector-sort/problem?isFullScreen=true

You are given a main function which reads the enumeration values for two different types as input, then prints out the corresponding enumeration names. Write a class template that can provide the names of the enumeration values for both types. If the enumeration value is not valid, then print unknown.

Input Format

The first line contains t, the number of test cases.
Each of the t subsequent lines contains two space-separated integers. The first integer is a color value, c, and the second integer is a fruit value, f.

Constraints

1 <= t <= 100
-2 x 10^9 <= c <= 2 x 10^9
-2 x 10^9 <= f <= 2 x 10^9

Output Format

The locked stub code in your editor prints t lines containing the color name and the fruit name corresponding to the input enumeration index.

Sample Input

2
1 0
3 3

Sample Output

green apple
unknown unknown

Explanation

Since t = 2, there are two lines of output.

The two input index values, 1 and 0, correspond to green in the color enumeration and apple in the fruit enumeration. Thus, we print green apple.
The two input values, 3 and 3, are outside of the range of our enums. Thus, we print unknown unknown.
*/

// Define a map for colors with corresponding integer values
unordered_map<int, string> colorMap {
    {0, "red"},
    {1, "green"},
    {2, "orange"}
};

// Define a map for fruits with corresponding integer values
unordered_map<int, string> fruitMap {
    {0, "apple"},
    {1, "orange"},
    {2, "pear"}
};

// Function to retrieve the name corresponding to a value from the map
string getEnumName(const unordered_map<int, string>& enumMap, int value) {
    // Check if the value exists in the map
    if (enumMap.find(value) != enumMap.end()) {
        return enumMap.at(value); // Return the name if found
    }
    return "unknown"; // If the name is not found
}


int main() {
    int t;
     cin >> t;
    
    // Process each test case
    while (t--) {
        int c, f;
        cin >> c >> f;
        
        // Get names using the lookup function
        string color = getEnumName(colorMap, c);
        string fruit = getEnumName(fruitMap, f);
        
        // Print the result
        cout << color << ' ' << fruit << endl;
    }
    
    return 0;
}
