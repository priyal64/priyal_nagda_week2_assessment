# •	5. Create a `Product` class with attributes 
# `name`, `price`, and `stock`. Write a method `check_availability(quantity)`
#  that returns whether the requested quantity is available.

class Product:
    dic={}
    # attributes 
# `name`, `price`, and `stock`
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
        self.dic[name]=stock
        # whether the requested quantity is available.
    def check_availability(self,name):
        if self.dic[name]>0:
            return "yes available"
        else:
            return "NOt available"

name=""
price=0 
stock=0 
c=Product(name,price,stock)
while(True):
    n=int(input("enter 1 for product details,2 for search ,3 for exit  "))
    if n==1:
        name=input("enter name of the product: ")
        price=int(input("Enter price of the item: "))
        stock=int(input("enter stock of the item: "))
        d=Product(name,price,stock)
    elif n==2:
        name=input("Enter name for chcking availability: ")
        print(c.check_availability(name))
    else:
        break
        
    
    



print(c.check_availability(name))