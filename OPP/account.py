class Account:
    def __init__(self, number, pin, owner_name, balance=0, overdraft_limit=0, interest_rate=0.0, minimum_balance=0):
        self.number = number
        self.__pin = pin
        self.owner_name = owner_name
        self.balance = balance
        self.overdraft_limit = overdraft_limit
        self.interest_rate = interest_rate
        self.minimum_balance = minimum_balance
        self.transaction_history = []
        self.frozen = False
        self.status = "active"
        self.__account_status = "Open"
    def account_status(self):
        return self.__account_status
    def view_account_details(self, pin):
        if pin == self.__pin:
            return f"Account Number: {self.number}\nOwner Name: {self.owner_name}\nBalance: {self.balance}\nStatus: {self.account_status()}"
        else:
            return "Wrong Pin"
    def   amount_withdrwal(self, withdraw):
         if withdraw <= self.__balance - self.minimum_balance:
            self.__balance-= withdraw
            self.transaction_history.append({"type": "withdraw", "amount": withdraw})
            print(f'New balance {self.__balance}')  
    def set_overdraft_limit(self, pin, new_limit):
        if pin == self.__pin:
            self.overdraft_limit = new_limit
            return "Overdraft limit is updated"
        else:
            return "Wrong Pin"
    def calculate_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        return f"Interest of {interest_amount} applied. New balance: {self.balance}"

    def apply_interest(self, rate):
        interest = self.calculate_interest(rate)
        self.__balance += interest
        print(f"Applied interest is {interest} new balance: {self.__balance}")
    def unfreeze_account(self, pin):
        if pin == self.__pin:
            self.frozen = False
            return "Account unfrozen "
        else:
            return "Wrong Pin"      
    def transaction_history(self):
        return self.transaction_history
    def set_minimum_balance(self, pin, new_minimum_balance):
        if pin == self.__pin:
            self.minimum_balance = new_minimum_balance
            return "Minimum balance requirement updated"
        else:
            return "Wrong Pin"
     def transaction_history(self):
         for i in self.transaction_history:
              print(f'{i['type']}: {i['amount']}')
    def transfer_fund(self, transfer_amount, owner_name):
         if transfer_amount > self.__balance:
              print(f' Transferred {transfer_amount} to {owner_name}')
         else:
              print("You have insufficient amount")       
    def close_account(self, pin):
        if pin == self.__pin:
            self.balance = 0
            self.status == 'active'
            if self.status == 'active':
              self.status == "closed"
              print("Account is closed")
         else:
              print("Account already closed")

           
        
          


   