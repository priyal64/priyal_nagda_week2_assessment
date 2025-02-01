# •	18. Implement an abstract class `ICalculator` 
# with methods `add()`, `subtract()`, `multiply()`, and `divide()`.
#  Create a `BasicCalculator` class that implements these methods.

from abc import ABC,abstractmethod
class ICalculator(ABC):
    def add(self):
        pass
    def subtract(self):
        pass
    def multiply(self):
        pass
    def divide(self):
        pass

class BasicCalculator(ICalculator):
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b!=0:
            return a/b
        
ob=BasicCalculator()
while(True):
    n=int(input("enter 1 for addition ,enter 2 for subtraction,3 for multiplication,4 for division and 5 to exit calculator"))
    
    if n!=5:
        a=int(input("Enter first value:"))
        b=int(input("enter second value"))
        if n==1:
            print("Addition is :",ob.add(a,b))
        elif n==2:
            print("subtraction is: ",ob.subtract(a,b))
        elif n==3:
            print("multiplication is: ",ob.multiply(a,b))
        elif n==4:
            print("division is: ",ob.divide(a,b))
        else:
            break
    else:
        break

                
