#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

/*
https://www.hackerrank.com/challenges/vector-sort/problem?isFullScreen=true

Given a text file with many lines of numbers to format and print, for each row of 3 space-separated doubles, format and print the numbers using the specifications in the Output Format section below.

Input Format

The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines describes a test case as 3 space-separated floating-point numbers: A, B, and C, respectively.

Output Format

For each test case, print 3 lines containing the formatted A, B, and C, respectively. Each A, B, and C must be formatted as follows:

A: Strip its decimal (i.e., truncate it) and print its hexadecimal representation (including the 0x prefix) in lower case letters.
B: Print it to a scale of 2 decimal places, preceded by a  or  sign (indicating if it's positive or negative), right justified, and left-padded with underscores so that the printed result is exactly 15 characters wide.
C: Print it to a scale of exactly nine decimal places, expressed in scientific notation using upper case.
Sample Input

1  
100.345 2006.008 2331.41592653498

Sample Output

0x64             
_______+2006.01  
2.331415927E+03
*/

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        double A, B, C;
        cin >> A >> B >> C;

        cout << "0x" << hex << nouppercase << (long long)A << endl; 

        cout << showpos << fixed << setprecision(2);
        cout << setw(15) << setfill('_') << B << endl;

        cout << uppercase << scientific << setprecision(9) << noshowpos;
        cout << C << endl;
    } 

    return 0;
}
