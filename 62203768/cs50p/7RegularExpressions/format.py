# Validate user input of Malan, David and output hello, David Malan

import re
# Request user input and strip whitespace
name = input("Full name: ").strip()
# Put the result in a variable if input str is like Malan,David, ask if True
if matches := re.search(r"^(.+), *(.+)$", name):
    # Swaps the 2 elements around and puts the result in a variable
    name = matches.group(2) + ' ' + matches.group(1)
# Says hello to the variable
print(f"hello, {name}")

# Explained

# One could want to
''' name = input("Name: ").strip()
        if ',' in name:
        last, first = name.split(", ")
        name = f"{first} {last}"
    print(f"hello, {name}")'''
# Unfortunately split doesn't support re so
''' import re
    name = input("Name: ").strip()'''
# .+ means something then , then space then something
# ^ means start matching from the start and $ the end
# The expression re.search(r"^.+, .+$", name) returns a value
# Put that in a variable so one can access the individual elements
''' matches = re.search(r"^.+, .+$", name)
    print(matches)
# Outputs None if given a valid input str'''
# Put the elements in distinct groups by adding parentheses
'''matches = re.search(r"^(.+), (.+)$", name)'''
# The first (.+) becomes matches.group(1) and the second (.+) matches.group(2)
# Add * meaning 0 or more of the preceding char to tolerate space or no space after the ,
''' matches = re.search(r"^(.+), *(.+)$", name)
# If true
    if matches:
        last, first = matches.groups()
        name = f"{first} {last}"'''
    # Which is nice but the walrus operator := allows us
    # Put the result in a variable if input str is like Malan,David, ask if True
''' if matches := re.search(r"^(.+), *(.+)$", name):'''
# Swaps the 2 elements around and puts the result in a variable
'''     name = matches.group(2) + ' ' + matches.group(1)'''
    # Is better
''' print(f"hello, {name}")'''
