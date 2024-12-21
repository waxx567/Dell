# Ask user for numbers
x = float(input("x: "))  # Input 999
y = float(input("y: "))  # Input 1

# Solution 1
# Variable to store rounded value of x + y to two decimal places
z = round(x / y, 2)
# Formatted strings can add formatting to the output
print(z)

# Solution 2
z = x / y
print(f"{z:.2f}")