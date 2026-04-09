class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount > self. __balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount

    def get_balance(self):
        print(f"Your current balance:{self.__balance}")

a1 = BankAccount(1000)
a1.deposit(500)
a1.withdraw(300)
a1.withdraw(2000)
a1.get_balance()


