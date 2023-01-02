class Batch:
     
  # Constructor
    def __init__(self, batchId, batchname, deptName, listofCourses, listofStudents):
        
        self.batchId=batchId
        self.batchname =batchname
        self.deptName = deptName
        self.listofCourses = listofCourses
        self.listofStudents= listofStudents
    
    # Function to create and append new batches
    def accept(self, batchId, batchname, deptName, listofCourses, listofStudents):
   
  # use ' int(input()) ' method to take input from user
        ob = Batch(batchId, batchname, deptName, listofCourses, listofStudents)
        ls.append(ob)
 
    # Function to display batch details
    def display(self, ob):
        print("batchId : ", ob.batchId)
        print("batchname : ", ob.batchname)
        print("deptName : ", ob.deptName)
        print("listofCourses : ", ob.listofCourses)
        print("listofStudents : ", ob.listofStudents)
        print("\n")
# Create a list to add Batches
ls = []
# an object of batch class
obj = Batch('', 0, 0, 0,0)
 
print("\nOperations used, ")
print("\n1.Accept batch details\n2.Display batch Details\n3.Exit")

obj.accept("CSE22","CSE 2022-26","CSE","C001:C002","CSE2201")
obj.accept("CSE21","CSE 2021-25","CSE","C001:C002","CSE2101")
obj.accept("ECE22","ECE 2022-26","ECE","C002","ECE2201:ECE2202")
# elif(ch == 2):
print("\n")
print("\nBatch details\n")
for i in range(ls.__len__()):
    obj.display(ls[i])
 # else:
print("Thank You !")