# https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

# Task

# ABC is a right-angled triangle at B.
# Therefore, the angle ABC is a right angle.
# Point M is the midoint of hypothenuse AC.
# You are given the lengths AB and BC.
# Your task is to find the measure of angle MBC in degrees.

# Input Format

# The first line contains the length of side AB.
# The second line contains the length of side BC.

# Constraints

# 0 < AB <= 100
# 0 < BC <= 100
# Lengths AB and BC are natural numbers.

# Output Format

# Print the angle MBC in degrees.
# Note: Round the angle to the nearest integer.

import math

# Read input for sides AB and BC
ab = int(input())
bc = int(input())

# Calculate angle MBC using the arctangent function
# math.atan returns the angle in radians, convert to degrees
angle_mbc = math.degrees(math.atan(ab/bc))

# Print the angle rounded to the nearest integer with the degree symbol as an ASCII character
print(f"{round(angle_mbc)}\u00B0")