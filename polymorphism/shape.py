# •	13. Develop a `Shape` class with a method `area()`. 
# Implement `Square` and `Triangle` 
# classes that provide specific implementations for `area()`.

class Shape:
    def area(self):
        pass
class square(Shape):
    def area(self,side):
        print(" the area of the square is ",side*side)
class Triangle(Shape):
    def area(self,le,he):
        print("the area of the traingle is 1/2 length* breadth",(1/2*(le*he)))

t=Triangle()
t.area(4,5)

s=square()
s.area(5)
