# •	6. Implement a multi-level inheritance example where
#  `Vehicle` is a base class, 
# `Car` and `Bike` inherit from `Vehicle`
# , and `ElectricCar` inherits from `Car`.

class Vehicle:
    def have_wheels(self):
        print("yes i have wheels")
    def work_in_petrol(self):
        print("yes i work on petrol")
    def work_in_diesel(self):
        print("yes i work on diesel")
    def can_work_with_electric(self):
        print("yes i work with electricity")
    def can_fly(self):
        print("vehicles name aeroplane and helicopter can fly")
    def can_float(self):
        print("yes i do have boats and ship for moving in water")

class car(Vehicle):
    def have_wheels(self):
        return super().have_wheels()
    def work_in_petrol(self):
        return super().work_in_petrol()
    def work_in_diesel(self):
        return super().work_in_diesel()
    def can_work_with_electric(self):
        return super().can_work_with_electric()
class bike(Vehicle):
    def have_wheels(self):
        return super().have_wheels()
    def work_in_petrol(self):
        return super().work_in_petrol()
    def can_work_with_electric(self):
        return super().can_work_with_electric()
    
class electric_car(car):
    def have_wheels(self):
        return super().have_wheels()
    
    def can_work_with_electric(self):
        return super().can_work_with_electric()
    
v=Vehicle()
electric=electric_car()
electric.can_work_with_electric()
electric.have_wheels()


# wheel_4=car()
# wheel_2=bike()

