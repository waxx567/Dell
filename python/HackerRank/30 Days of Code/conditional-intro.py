# https://www.hackerrank.com/challenges/30-conditional-statements/problem?h_r=email&unlock_token=576dcb5f44804c35db83dd6fc207cf1b4a0917af

# Objective
# In this challenge, we learn about conditional statements. Check out the Tutorial tab for learning materials and an instructional video.

# Task
# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Complete the stub code provided in your editor to print whether or not  is weird.

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input().strip())

    if N % 2 != 0:
        print("Weird")
    elif N % 2 == 0 and 2 <= N <= 5:
        print("Not Weird")
    elif N % 2 == 0 and 6 <= N <= 20:
        print("Weird")
    elif N % 2 == 0 and N > 20:
        print("Not Weird")