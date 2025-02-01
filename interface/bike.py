# •	19. Develop an interface `IVehicle` 
# with abstract methods `start_engine()`
#  and `stop_engine()`. Implement it in `Car`, `Bike`, and `Truck` classes.
from abc import ABC,abstractmethod
class IVehicle(ABC):
    def start_engine(self):
        pass
    def stop_engine(self):
        pass


# Implement it in `Car`, `Bike`, and `Truck` classes.
class Car(IVehicle):
    def start_engine(self):
        print("this is the first step in while driving the car: ")
    def then_were_seat_belt(self):
        print("before that were seat belt")
    def stop_engine(self):
        print("when at signal please stop the engine...")
class Bike(IVehicle):
    def start_engine(self):
        print("in bike sometimes we use kick option to start engine....")
    def wearing_helmet(self):
        print("we wear helmet when driving bike...")
    def stop_engine(self):
        print("please stop the vehicle during signal")

class Truck(IVehicle):
    def start_engine(self):
        print("i am truck , and i can start whenever i wishes for")
    def waering_seat_belt(self):
        print("wearing seat belt i feel is not necessary...")
    def stop_engine(self):
        print("i will stop when someone ask for lift")
t=Truck()
t.stop_engine()

c=Car()
c.start_engine()

b=Bike()
b.start_engine()