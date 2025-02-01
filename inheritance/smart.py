# •	10. Build a `SmartPhone` class inheriting from `MobileDevice`, 
# which in turn inherits from `Electronics`.
#  Demonstrate method overriding and attribute reuse.
class Electronics:
    def i_use_electricity(self):
        print("Electronics use electricity to function or charge.")

class MobileDevice(Electronics): 
    def i_can_call(self):
        print("This device can make calls.")
    def i_have_calculator(self):
        print("This device has a basic calculator.")
    def can_show_time(self):
        print("This device can show time.")

class SmartPhone(MobileDevice):
    def i_can_call(self):
        print("I am a smartphone. I can make video and voice calls!")
    def i_have_apps(self):
        print("I have a touchscreen and can run various apps.")

    def i_am_smart(self):
        print("I am a smart device with internet connectivity.")

# Creating an object of SmartPhone
ob = SmartPhone()

ob.i_use_electricity()  
ob.i_can_call()        
ob.i_have_calculator() 
ob.can_show_time()     
ob.i_have_apps()        
ob.i_am_smart()       
