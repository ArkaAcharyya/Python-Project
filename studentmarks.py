count=int(input("how many students are there?"))
fileout=open("Stuent.dat","w")
for i in range(count):
    print("Enter details for student",(i+1),"below:")
    rollno=int(input("Roll no:"))
    name=input("Name:")
    marks=float(input("Marks:"))
    grade=input("Enter the grade:")
    rec=str(rollno)+","+name+","+str(marks)+grade+'\n'
    fileout.write(rec)
fileout.close()