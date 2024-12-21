# TODO

import cs50

def main():

    # Get card number from user
    card_num = cs50.get_int("Number: ")
    # Saves card_num intact and creates chop_num to parse for validation calculation
    chop_num = card_num

    # Creates empty lists to store numbers parsed from chop_num
    num_1 = []
    num_2 = []

    # Parse credit card number and put values in num_1 and num_2 lists
    while chop_num > 10:
        # Select final digit and place in num_1
        num_1.append(chop_num % 10)
        # Remove final digit from chop_num
        chop_num = int(chop_num / 10)
        # Select final digit from shortened chop_num, place in num_2
        num_2.append(chop_num % 10)
        # Remove final digit from chop_num
        chop_num = int(chop_num / 10)

    # Multiply values in num_2 by 2 and place new values in num_3
    num_3 = []
    for i in num_2:
        i = i * 2
        num_3.append(i)

    # Split values over 10 into constituent parts and place all in num_4
    num_4 = []
    for i in num_3:
        if i >= 10:
            i_2 = i - 10
            num_4.append(1)
            num_4.append(i_2)
        if i < 10:
            num_4.append(i)

    # Check that total of relevant lists is a multiple of 10 or else invalidate
    x = sum(num_1) + sum(num_4)
    if x % 10 != 0:
        print("INVALID")

    # Variable to store amount of digits in original number
    length = len(num_1) + len(num_2)
    # Creates string version of card_num for parsing in validations
    str_num = str(card_num)

    # Validate Amex
    if length == 15:
        if str_num[0] == '3':
            if str_num[1] == '4' or str_num[1] == '7':
                print("AMEX")

    # Validate Mastercard
    if length == 16:
        if str_num[0] == '5':
            if str_num[1] in ['1', '2', '3', '4', '5']:
                print("MASTERCARD")

    # Validate Visa
    if length == 13 or length == 16:
        if str_num[0] == '4':
            print("VISA")
    else:
        print("INVALID")

main()