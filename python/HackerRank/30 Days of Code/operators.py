# DAY 2

# https://www.hackerrank.com/challenges/30-operators/problem?h_r=email&unlock_token=41861bc82787225ab738d811a07207e796d2b671&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder

# Objective
# In this challenge, you will work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video.

# Task
# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. Round the result to the nearest integer.

# A tip of 15% * 100 = 15, and the taxes are 8% * 100 = 8. Print the value 123 and return from the function.

# Function Description
# Complete the solve function in the editor below.

# solve has the following parameters:

# int meal_cost: the cost of food before tip and tax
# int tip_percent: the tip percentage
# int tax_percent: the tax percentage
# Returns The function returns nothing. Print the calculated value, rounded to the nearest integer.

# Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip = meal_cost * tip_percent / 100
    print("The tip is", tip)
    tax = meal_cost * tax_percent / 100
    print( "The tax is", tax)
    total = meal_cost + tip + tax
    
    print(round(total))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
