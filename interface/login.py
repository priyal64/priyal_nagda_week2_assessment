# •	20. Write a scenario
#  where a `UserAuthentication` interface contains 
# `login()` and `logout()` 
# methods, and it is implemented by `GoogleAuth` and `FacebookAuth` classes.
from abc import ABC,abstractmethod
class UserAuthentication:
    def login(self):
        pass
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def login(self,name,email,password):
        print("please enter details: ")
        print("you are logged in")
    def logout(self):
        print(" you are logged out ,thank you for visiting")

class Facebookauth(UserAuthentication):
    def login(self,name,email,password):
        print("please enter details: ")
        print("you are logged in")
    def logout(self):
        print(" you are logged out ,thank you for visiting")
f=Facebookauth()
f.login("plll","mail.com","password")
g=GoogleAuth()
g.logout()