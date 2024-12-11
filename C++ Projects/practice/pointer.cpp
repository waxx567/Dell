#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/*
https://www.hackerrank.com/challenges/c-tutorial-pointer/problem?isFullScreen=true

A pointer in C++ is used to share a memory address among different contexts (primarily functions). They are used whenever a function needs to modify the content of a variable, but it does not have ownership.

Function Description

Complete the update function in the editor below.

update has the following parameters:

int *a: an integer
int *b: an integer

Returns

The function is declared with a void return type, so there is no value to return. Modify the values in memory so that `a` contains their sum and `b` contains their absoluted difference.

Input Format

Input will contain two integers, a and b, separated by a newline.

Sample Input

4
5

Sample Output

9
1
*/

void update(int *a, int *b);

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int a, b;
    cin >> a >> b;
    
    update(&a, &b);

    cout << a << endl << b << endl;
    
    return 0;
}

void update(int *a, int *b) {
    int sum = *a + *b;
    int diff = abs(*a - *b);
    *a = sum;
    *b = diff;
}