class InsufficientFundsError(Exception):
    pass
class Account:
    
    def __init__(self,owner,balance=0):
        print("welcome ")
        self.owner=owner
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    
    def withdraw(self,amount):
        if(amount>self.balance):
            raise InsufficientFundsError(f"Insufficient fund Your balance is {self.balance} but you requested {amount}")
        else:
            self.balance-=amount
            
    def show(self):
        return  self.balance          
     
acc=Account("Arun",1000)
try:
    acc.deposit(500)
    print(acc.owner," Your Bank Balance is ",acc.show())
    acc.withdraw(2000)
except InsufficientFundsError as e:
    print("Error : ", e)
    
finally:
    print("Transaction completed")


class SavingsAccount(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
    def withdraw(self, amount):
        if((self.balance-amount)<500 or amount>self.balance):
            raise InsufficientFundsError(f"Insufficient fund Your balance is {self.balance} but you requested {amount}")
        else:
            self.balance-amount

sa=SavingsAccount("Priya",500)
try:
    acc.deposit(500)
    print(sa.owner," Your Bank Balance is ",sa.show())
    sa.withdraw(300)
except InsufficientFundsError as e:
    print("Error : ", e)
    
finally:
    print("Transaction completed")

print(isinstance(sa, Account))