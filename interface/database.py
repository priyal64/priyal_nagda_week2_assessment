# Define an abstract class `IDatabaseOperations`
#  with methods `insert()`, `update()`, and `delete()`.
#  Implement this in `SQLDatabase` and `NoSQLDatabase`.

from abc import ABC,abstractmethod
class IDatabaseOperations(ABC):
    def insert(self):
        pass
    def delete(self):
        pass
    def update(self):
        pass

class SQLDatabase(IDatabaseOperations):
    def insert(self,ins_val):
        print("the value is inserted in mysqldb")
    def delete(self,del_val):
        print("the value is deleted")
    def update(self,old,new_v):
        print("the new value is updated...")
class NOSQLDatabase(IDatabaseOperations):
    def insert(self,ins_val):
        print("the value is inserted to the database")
    def delete(self):
        print("the value is deleted")
    def update(self,new_v,old):
        print("the value is updated to new value...")

nos=NOSQLDatabase()
nos.insert(11)

so=SQLDatabase()
so.update(11,12)
        
        
        