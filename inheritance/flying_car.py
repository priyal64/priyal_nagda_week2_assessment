# •	9. Simulate multiple inheritance where `FlyingCar`
#  inherits from both `Car` and `Airplane`. 
# Handle potential conflicts in the `move()` method.
class Car:
    def move(self):
        print("I move on the road.")
    def wheels(self):
        print("I have 4 wheels.")

class Airplane:
    def move(self):
        print("I fly in the sky.")
    def can_travel_globally(self):
        print("I can go anywhere in the world.")

class FlyingCar(Car, Airplane):  
    def move(self, mode="road"):
        if mode == "road":
            super().move()  # Calls Car's move method
        elif mode == "sky":
            Airplane.move(self)  
        else:
            print("Invalid mode. Choose 'road' or 'sky'.")

# Create an instance of FlyingCar
f = FlyingCar()

# Test the functionality
f.move("road")
f.move("sky")
f.wheels()
f.can_travel_globally()
