# 
# https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

# Task
# You are given a complex . Your task is to convert it to polar coordinates.

# Constraints

# Given number is a valid complex number

# Sample Input

#   1+2j

# Sample Output

#  2.23606797749979 
#  1.1071487177940904

# Note: The output should be correct up to 3 decimal places.
# 

import cmath

r = complex(input())

print(abs(r))
print(cmath.phase(r))