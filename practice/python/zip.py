# Zip

names = ['tim', 'joe', 'billy', 'sally']
ages = [21, 19, 18, 43]
eye_color = ['blue', 'brown', 'brown', 'green']

print(list(zip(names, ages, eye_color)))    # Prints list of tuples

for name, age in zip(names, ages):
    if age > 20:
        print(name)