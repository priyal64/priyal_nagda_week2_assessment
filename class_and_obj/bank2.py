# Design a `BankAccount` class with `deposit()` and `withdraw()` methods. 
# Implement logic to prevent overdraft.

class BankAccount:
    def deposit(self,account,dep_val):
        account+=dep_val
        print(" money deposited: ")
        print(" your new balance is: ",account)
    def withdraw(self,account,with_draw):
        if with_draw<=account:
            account-=with_draw
            print(" money withdrawn ")
            print(" new balance is: ",account)

# Creating an instance of the BankAccount class
obj=BankAccount()
account=99999
# with_draw=1212
# dep_val=1000
n=int(input("Enter 1 for deposit and 2 for withdrawl"))
if n==1:
    dep_val=int(input("enter deposit value: "))
    obj.deposit(account,dep_val)
else:
    with_draw=int(input(" enter withdrawl amount: "))
    obj.withdraw(account,with_draw)