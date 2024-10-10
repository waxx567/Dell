# Reverse an input string

x = input("Type string you want to reverse: ")
# If you want the reversed string saved in a variable
b = ''.join(reversed(x))
print(b)
# Or use a start end step which slices string by steps of -1 if you don't
print(x[::-1])