''' 
Implement a program in Python that prompts the user for mass as an integer 
(in kilograms) and then outputs the equivalent number of Joules as an integer.
Assume that the user will input an integer.

E = mc^2

E is Energy (output)
m is mass (input)
c is the speed of light

c = 300000000m/s
'''

# Get user input, convert it to an integer and store in kilos variable
kilos = int(input("m:  "))

# Calculate joules as per E = mc^2
joules = kilos * (300000000 * 300000000)

# Print rounded result
print(f"E: {round(joules)}")