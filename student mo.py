 # Create class "Student"
class Student:
 
  # Constructor
    def __init__(self, id, name, rollno, batchname):
        self.id=id
        self.name = name
        self.rollno = rollno
        self.batchname=batchname
        
    # Function to create and append new student
    def accept(self, Id, Name, Rollno, Batchname):
   
  # use ' int(input()) ' method to take input from user
        ob = Student(Id, Name, Rollno, Batchname)
        ls.append(ob)
 
    # Function to display student details
    def display(self, ob):
        print("Id : ", ob.id)
        print("Name : ", ob.name)
        print("RollNo : ", ob.rollno)
        print("Batchname : ", ob.batchname)
        print("\n")
 
    # Search Function
    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i
 
    # Delete Function
    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]
 
    # Update Function
    def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        
        
 
 
# Create a list to add Students
ls = []
# an object of Student class
obj = Student('', 0, 0, 0)
 
print("\nOperations used, ")
print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")
 
# ch = int(input("Enter choice:"))
# if(ch == 1):
obj.accept("CSE2201", "SUMIT AGGARWAL", 1, 'CSE22')
obj.accept("CSE2101", "AMAN VERMA", 1, 'CSE21')
obj.accept("ECE2201", "ROHIT GUPTA", 1, 'ECE22')
obj.accept("ECE2202", "VISHAL KUMAR", 2, 'ECE22')
 
# elif(ch == 2):
print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
    obj.display(ls[i])
 
# elif(ch == 3):
print("\n Student Found, ")
s = obj.search(2)
obj.display(ls[s])
 
# elif(ch == 4):
obj.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):
    obj.display(ls[i])
 
# elif(ch == 5):
obj.update(3, 2)
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):
    obj.display(ls[i])
# else:
print("Thank You !")


