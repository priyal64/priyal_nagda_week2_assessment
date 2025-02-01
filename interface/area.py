# •	16. Create an interface `IShape` 
# with an abstract method `calculate_area()`.
#  Implement it in `Rectangle` and `Circle` classes.
from math import pi
from abc import ABC,abstractmethod
#  method `calculate_area()
class Interface(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
#  Implement it in `Rectangle` and `Circle` classes.
class Rectangle(Interface):
    def calculate_area(self,s1,s2):
        print("the rectangular area of side{s1} and {s2} is:",s2*s1)

class Circle(Interface):
    def calculate_area(self,radius):
        print("the area of the circle is: ",pi*radius*radius)

c=Circle()
c.calculate_area(3)

r=Rectangle()
r.calculate_area(4,5)