# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

# Consider the following:

# A string, s, of length n where c^0c^1...c^n-1.
# An integer, k, where k is a factor of n.
# We can split s into n/k substrings where each subtring, t^i, consists of a contiguous block of k characters in s. Then, use each t to create string u^i such that:

# The characters in u^i are a subsequence of the characters in t^i.
# Any repeat occurrence of a character is removed from the string such that each character in u^i occurs exactly once. In other words, if the character at some index j in t occurs at a previous index <j in t, then do not include the character in string u^i.
# Given s and k, print n/k lines where each line i denotes string u^i.

# Example

# s = "AAABCADDE"
# k = 3

# There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so u^1 = 'A'. The second substring has all distinct characters, so u^2 = 'BCA'. The third substring has 2 different characters, so u^3 = 'DE'. Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.

# Function Description

# Complete the merge_the_tools function in the editor below.

# merge_the_tools has the following parameters:

# string s: the string to analyze
# int k: the size of substrings to analyze

# Prints

# Print each subsequence on a new line. There will be n/k of them. No return value is expected.

# Input Format

# The first line contains a single string, s.
# The second line contains an integer, k, the length of each substring.

# Constraints

# 1 <= n <= 10^4, where n is the length of s
# 1 <= k <= n
# It is guaranteed that n is a multiple of k.

# Sample Input

# STDIN       Function
# -----       --------
# AABCAAADA   s = 'AABCAAADA'
# 3           k = 3

# Sample Output

# AB
# CA
# AD

# Explanation

# Split s into n/k = 9/3 = 3 equal parts of length . Convert each t^i to u^i by removing any subsequent occurrences of non-distinct characters in t^i:

# t^0 = AAB -> u^0 = AB
# t^1 = CAA -> u^1 = CA
# t^2 = ADA -> u^2 = AD

# Print each u^i on a new line.

def merge_the_tools(string, k):
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)