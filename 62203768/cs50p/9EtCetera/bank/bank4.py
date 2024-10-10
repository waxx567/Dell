# Using Object-oriented Programming
class Account:
    def __init__(self):
        self._balance = 0
        # Rememeber: putting an underscore before the variable indicates that is not to be tampered with

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print("Balance: ", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance: ", account.balance)


if __name__ == "__main__":
    main()

# Balance: 0
# Balance: 50

# This works because the instance variables are accessible to all of the methods in that class via the parameter self
# The other way is probably better for a small application like this but this shows a structure for more complicated code