# Demo of try-except
try:
    year = int(input("Year: "))
    leap_or = year % 4 == 0
    # Input 1976 returns:
    if leap_or:
        print("This is a leap year")
    # Input 1999 returns:
    else:
        print("This is not a leap year")
# Input nineteen eighty four returns:
except ValueError:
    print("Only digits are allowed!")

# Multiple except statements examples
num_list = [5, 'c', 20, 0, 40]
b = 15
for x in num_list:
    # Input of integer returns:
    try:
        c = b / x
        print(c)
    # Input 0.75 returns:
    except ZeroDivisionError:
        print("An element with 0 value")
    # Input 3.0 returns:
    except TypeError:
        print("Only numbers can be used")

# An example of else clause with try-except
try:
    a_number = int(input('Your Number? '))
# Input str returns:
except:
    print('Enter a Number.')
else:
    eve_or_odd = a_number % 2 == 0
    # Input 456 returns:
    if eve_or_odd:
        print('You entered an even number.')
    # Input 007 returns:
    else:
        print('An odd number.')

# The finally clause will execute in all circumstances. Whether an error occurs or not the finally clause execute before leaving the try statement.
try:
    a_number = int(input('Your Number? '))
except:
    print('Enter a Number.')
else:
    eve_or_odd = a_number % 2 == 0
    if eve_or_odd:
        print('You entered even number.')
    else:
        print('An Odd number.')
finally:
    print("Thank you for using the program.")
# The general use of finally clause is releasing the external resources e.g. closing a database connection, closing a file etc. whether program ran successfully or not.