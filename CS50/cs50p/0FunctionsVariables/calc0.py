# Ask user for numbers
x = float(input("x: "))  # Input 999
y = float(input("y: "))  # Input 1
# Variable to store rounded value of x + y
z = round(x + y)
# Formatted strings can add formatting to the output
print(f"{z:,}")