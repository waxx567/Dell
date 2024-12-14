# You are given a positive integer N.
# Your task is to print a palindromic triangle of size N.

# For example, a palindromic triangle of size 5 is:

# 1
# 121
# 12321
# 1234321
# 123454321

# You can't take more than two lines. The first line (a for-statement) is already written for you.

# You have to complete the code using exactly one print statement.

# Note:
# Using anything related to strings will give a score of 0.
# Using more than one for-statement will give a score of 0.

# Input Format

# A single line of input containing the integer n.

# Constraints

# 0 < n <= 10

# Output Format

# Print the palindromic triangle of size N as explained above.

# Sample Input

# 5

# Sample Output

# 1
# 121
# 12321
# 1234321
# 123454321

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i-1)//9)**2

# Explanation:

# The expression `((10**i-1)//9)**2` generates the numbers needed to form the palindromic triangle in a single print statement. Here's how it works:

### Breakdown of the Expression:
# 1. **`10**i`**: 
#    - This raises 10 to the power of `i`. 
#    - For example, when `i = 3`, `10**3 = 1000`.

# 2. **`10**i - 1`**:
#    - Subtracting 1 creates a number of repeated 9s.
#    - Example: `10**3 - 1 = 1000 - 1 = 999`.

# 3. **`(10**i - 1) // 9`**:
#    - Dividing by 9 converts the number of repeated 9s into a number made of repeated digits of `1`.
#    - Example: `999 // 9 = 111`.

# 4. **`((10**i - 1) // 9)**2`**:
#    - Squaring this value generates the palindromic number.
#    - Example: When `i = 3`, the value is `111`, and `111**2 = 12321`.

### Why It Works:
# - The expression generates numbers in the sequence:
#   - `i = 1`: `(10**1 - 1) // 9 = 1`, and `1**2 = 1`
#   - `i = 2`: `(10**2 - 1) // 9 = 11`, and `11**2 = 121`
#   - `i = 3`: `(10**3 - 1) // 9 = 111`, and `111**2 = 12321`
#   - `i = 4`: `(10**4 - 1) // 9 = 1111`, and `1111**2 = 1234321`
#   - `i = 5`: `(10**5 - 1) // 9 = 11111`, and `11111**2 = 123454321`

### Mathematical Insight:
# - Squaring a number consisting of repeated `1`s (like `1`, `11`, `111`) produces palindromic numbers due to the multiplication pattern inherent in such numbers.

# This compact mathematical trick allows the creation of the desired pattern using only one print statement, adhering to the problem's constraints.