# https://www.hackerrank.com/challenges/python-quest-1/problem?isFullScreen=true

# You are given a positive integer N. Print a numerical triangle of height N-1 like the one below:

# 1
# 22
# 333
# 4444
# 55555
# ......

# Can you do it using only arithmetic operations, a single for loop and print statement?

# Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.

# Note: Using anything related to strings will give a score of 0.

# Input Format

# A single line containing integer, N.

# Constraints

# 1 <= N <= 9

# Output Format

# Print  lines as explained above.

# Sample Input

# 5

# Sample Output

# 1
# 22
# 333
# 4444

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i // 9) * i)

# The key to solving this problem is leveraging arithmetic operations rather than strings. You can use mathematical expressions involving `i` and powers of 10 to create the desired pattern.

# Here’s the completed `print` statement:

# ```python
# for i in range(1, int(input())): 
#     print((10**i // 9) * i)
# ```

# ### Explanation:
# - `10**i` raises 10 to the power of `i`.
# - `10**i // 9` generates numbers like 1, 11, 111, 1111, corresponding to repeating 1s.
# - Multiplying this by `i` results in rows like:
#   - `1 * 1 = 1`
#   - `11 * 2 = 22`
#   - `111 * 3 = 333`
#   - `1111 * 4 = 4444`

# This approach avoids strings and uses only arithmetic operations.