class Department:
     
  # Constructor
    def __init__(self, batchId, deptName, listofBatches):
        
        self.batchId=batchId
        self.deptName = deptName
        self.listofBatches = listofBatches
        
    # Function to create and append new departments
    def accept(self, batchId, deptName, listofBatches):
   
  # use ' int(input()) ' method to take input from user
        ob = Department(batchId, deptName, listofBatches)
        ls.append(ob)
 
    # Function to display dept details
    def display(self, ob):
        print("batchId : ", ob.batchId)
        print("deptName : ", ob.deptName)
        print("listofBatches : ", ob.listofBatches)
        print("\n")
# Create a list to add Department
ls = []
# an object of department class
obj = Department('', 0, 0)
 
print("\nOperations used, ")
print("\n1.Accept dept details\n2.Display dept Details\n3.Exit")

obj.accept("CSE","Computer Science and Engineering","CSE22:CSE21")
obj.accept("ECE","Electronics and Communication Engineering","ECE22")
# elif(ch == 2):
print("\n")
print("\nDept details\n")
for i in range(ls.__len__()):
    obj.display(ls[i])
 # else:
print("Thank You !")