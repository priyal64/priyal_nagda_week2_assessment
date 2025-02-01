# •	8. Design a system where a base class `Animal` 
# has a method `speak()`,
#  and subclasses `Dog` and `Cat` override it.

class Animal:
    def speak(self):
        pass
    def have_4_legs(self):
        print("yes i have 4 legs")


class Dog(Animal):
    def speak(self):
        print("Dog i bark!")
    
class Cat(Animal):
    def speak(self):
        print(" cat: i say meow")

# cat object
ob=Cat()
ob.speak()
ob.have_4_legs()

o=Dog()
o.speak()