class Account:
    def __init__(self,number,pin):
        self.number=number
        self._pin= pin
        self._balance= 0

    def show_balance(self,pin):
        if pin ==self.__pin:
            return self._balance
        else:
            return "wrong pin"
    class Account:
     def __init__(self,number,pin,baance):
        self.number=number
        self.pin=pin
        self.__balance=0
def show_balance(self,pin):
    if pin==self .__pin:
        return self.__balance
    else:
        return "wrong pin" 
class BankAccount:
    def __init__(self, first_name, last_name, balance=0.0):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} made. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} made. New balance: {self.balance}")
        else:
            print("Insufficient balance. Withdrawal declined.")

    def view_account_details(self):
        print(f"Account Owner: {self.first_name} {self.last_name}")
        print(f"Current Balance: {self.balance}")

    def change_account_owner(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        print(f"Account owner updated to {first_name} {last_name}")

    def account_statement(self):
        print("Account Statement:")
        print(f"Account Owner: {self.first_name} {self.last_name}")
        print(f"Current Balance: {self.balance}")

    def set_overdraft_limit(self, limit):
        self.overdraft_limit = limit
        print(f"Overdraft limit set to {limit}")

    def interest_calculation(self, rate):
        interest = self.balance * rate
        self.balance += interest
        print(f"Interest calculated. New balance: {self.balance}")

    def freeze_account(self):
        self.frozen = True
        print("Account frozen.")

    def unfreeze_account(self):
        self.frozen = False
        print("Account unfrozen.")

    def transaction_history(self):
        print("Transaction History:")
        

    def set_minimum_balance(self, minimum_balance):
        self.minimum_balance = minimum_balance
        print(f"Minimum balance set to {minimum_balance}")

    def transfer_funds(self, other_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print(f"Transfer of {amount} made to {other_account.first_name} {other_account.last_name}. New balance: {self.balance}")
        else:
            print("Insufficient balance. Transfer declined.")

    def close_account(self):
        print("Account closed. All operations terminated.")
     










        


    
    