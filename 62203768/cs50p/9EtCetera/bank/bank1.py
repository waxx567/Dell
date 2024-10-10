balance = 0


def main():
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    print("Balance: ", balance)


def deposit(n):
    balance += n


def withdraw(n):
    balance -= n


if __name__ == "__main__":
    main()

# This throws UnboundLocalError: local variable 'balance' referenced before assignment
# Slightly misleading because balance was assigned before on line 1
# However that assignment is outside the main function ie. it needs to be local to the function

# So you can read a global variable but you can't write to a global variable