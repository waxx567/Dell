def main():
    balance = 0
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

# BUT this throws the exact same error
# because the deposit and withdraw functions do not have access to that variable because it is local to main