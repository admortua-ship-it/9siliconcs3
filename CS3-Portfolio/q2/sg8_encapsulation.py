class BackAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_balance(self, balance):
        if balance < 0:
            print("The balance must not be a negative number.")
        else:
            self.__balance = balance

    @property
    def get_account_number(self):
        return self.__account_number

    @property
    def get_balance(self):
        return self.__balance

# Output

a1 = BackAccount("12345", 1000)

print("Account 1")
print("Account Number:", a1.get_account_number)
print("Balance:", a1.get_balance)

print("\nUpdate balance to -100")
new_balance = a1.set_balance(-100)
print("Account Number:", a1.get_account_number)
print("Balance:", a1.get_balance)