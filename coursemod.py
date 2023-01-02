class Course:
     
  # Constructor
    def __init__(self, courseId, coursename, studentId, marksObtained):
        
        self.courseId=courseId
        self.coursename =coursename
        self.studentId = studentId
        self.marksObtained=marksObtained
    
    # Function to create and append new course
    def accept(self, courseId, coursename, studentId, marksObtained):
   
  # use ' int(input()) ' method to take input from user
        ob = Course(courseId, coursename, studentId, marksObtained)
        ls.append(ob)
 
    # Function to display course details
    def display(self, ob):
        print("courseId : ", ob.courseId)
        print("coursename : ", ob.coursename)
        print("studentId : ", ob.studentId)
        print("marksObtained : ", ob.marksObtained)
        print("\n")
# Create a list to add COURSES
ls = []
# an object of course class
obj = Course('', 0, 0, 0)
 
print("\nOperations used, ")
print("\n1.Accept course details\n2.Display course Details\n3.Exit")

obj.accept("C001","PYTHON PROGRAMMING","CSE2201","95")
obj.accept("C002","PHYSICS","CSE2201","78")
obj.accept("C003","CHEMISTRY","CSE2201","91")
# elif(ch == 2):
print("\n")
print("\nCourse details\n")
for i in range(ls.__len__()):
    obj.display(ls[i])
 # else:
print("Thank You !")