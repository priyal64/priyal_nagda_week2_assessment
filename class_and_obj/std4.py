# •	4. Implement a `Student` class with a constructor that 
# initializes `name` and `roll_number`
# . Write a method to return student details

class Student:
    # initializes `name` and `roll_number`
    def __init__(self,sname,sroll):
        self.sname=sname
        self.sroll=sroll
        print("the details of students:")
        
# . Write a method to return student details
    def display(self):
        print("name of the student is: ",self.sname)
        print("and their roll number is: ",self.sroll)
        lis.append([self.sname,self.sname])
        return lis

# storing it in lists
lis=[]
while(True):
    n=int(input("enter 1 for entering details of student"))
    if n==1:
        sname=input("Enter name of the student: ")
        sroll=int(input("Enter id of the student: "))
        s=Student(sname,sroll)
        
    else:
        break
    lis.append(s.display())
    
print(lis)