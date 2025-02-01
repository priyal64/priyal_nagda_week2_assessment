# •	3. You are building a Library Management System. Create a `Book` 
# class with properties like `title`, `author`, and `isbn`. 
# Write a method to display book details.

class Book:
    def display(self,lis):
        for x in lis:
            print(" the title of the book is: ",x[0],"and the author of the book is: ",x[1])

# object (instance creation)
b=Book()
lis=[]
while(True):
    n=int(input("enter 1 for entering details of books"))
    if n==1:
        title=input("Enter title of the book: ")
        author=input("Enter author of the book: ")
        lis.append([title,author])
    else:
        break
    
b.display(lis)