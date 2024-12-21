'''
In Massachusetts, home to Harvard University, it`s possible to str_in a vanity license plate for your car,
with your choice of letters and numbers instead of random ones.
Among the requirements, though, are: “All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end.
For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a `0`.”
“No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the
requirements or Invalid if it does not. Assume that any letters in the user`s input will be uppercase.
Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
Assume that s will be a str. You`re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
'''


def main():

  # Prompt user
  plate = input("Plate: ")

  # Call function to validate input, print result
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")


# Function to validate user input
def is_valid(str_in):

  # check if length within range
  if len(str_in) < 2 or len(str_in) > 6:
    return False

  # check if 1st two characters are both letters
  if str_in[0].isalpha() == False or str_in[1].isalpha() == False:
    return False

  # ensure 1st number is not zero
  count = 0
  while count < len(str_in):
    if str_in[count].isdigit():
      if str_in[count] == '0':
        return False
      else:
        break
    count += 1

  # check input does not contain periods, spaces, or punctuation marks
  for char in str_in:
    if char in [' ', '.', ',', '?', '!']:
      return False

  # all checks passed
  return True



# Call main function
if __name__ == "__main__":
    main()