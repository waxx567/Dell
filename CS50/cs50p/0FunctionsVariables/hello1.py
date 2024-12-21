# Ask user for name
name = input("What's your name? ").strip().upper()
# Split user's name into first and last name
first, last = name.split(" ")
# Say hello to user by their first name
print(f"hello, {first}")