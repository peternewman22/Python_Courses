"""
Note: class variables = shared by any instance = no self
Instance variables are defined per instance. have self at the beginning.
Docstrngs are called by instance.__doc___
"""


class Account:
    """ This tells you what a class does """

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def display_balance(self):
        print(self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, "w") as file:
            file.write(str(self.balance))


"""
We're going to use inheritance
"""


class Checking(Account):
    """This tells you what the class does"""
    tf_Fee = 1 # this is a class variable shared by all instances of a class
    def __init__(self, filepath):
        Account.__init__(self, filepath)

    def transfer(self, amount):
        self.balance = self.balance - amount - tf_fee

account = Account("balance.txt")
print(account.__doc__)
#account.display_balance()
#account.withdraw(100)
#account.display_balance()
#account.deposit(150)
#account.display_balance()
#account.commit()
