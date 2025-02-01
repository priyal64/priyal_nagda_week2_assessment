# •	7. Create a multi-level class structure with `Person` → `Employee` → `Manager`,
#  where `Manager` has an additional method `approve_leave()`.


# multilevel class
class Person:
    def __init__(self):
        pass
    def is_person(self):
        print("yes is a person")
class Employee(Person):
    def is_person(self):
        return super().is_person()
    def get_salary(self):
        pass
    def role(self):
        pass
    #  where `Manager` has an additional method `approve_leave()`.
class Manager(Employee):
    def __init__(self,salary):
        self.salary=salary

    def is_person(self):
        return super().is_person()
    def get_salary(self):
        print("the salary of the manager is: ",self.salary)
    def approve_leave(self):
        n=int(input("enter 1 for approval of leave or 2"))
        if n==1:
            print("leave approved")
        else:
            print("no leave")

# objects instance
ob=Manager(1200000)
ob.get_salary()
ob.approve_leave()    

x=Employee()