# Create a class `Employee` with properties `name`, `id`, and `department`.
#  Instantiate an object and assign values dynamically.

class Employee:
    
    def __init__(self,name,id,department,emp_lis):
        self.lis=[]
        self.name=name
        self.id=id
        self.department=department
        print("name: ",self.name,", id: ",self.id,", department: ",self.department)
        self.lis.append([self.name,self.id,self.department])
        emp_lis.append(self.lis)

# ob=Employee()
emp_lis=[[]]
emp_lis.append(["name ","id "," department"])
while(True):
    n=int(input("Enter 1 for giving values: "))
    if n==1:
        name=input("enter your name: ")
        id=input("Enter id: ")
        department=input("enter department: ")
        ob=Employee(name,id,department,emp_lis)
    else:
        break

print(emp_lis)


