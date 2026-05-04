file=open("prg14.txt","r")

emp_no=int(input("Enter Emp_no :"))
print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<10} {:<10}".format("Emp_no","Name","Dept_no","Basic","DA","HRA","Conveyance","Net Salary"))

for line in file:
	value=line.split()
	if(str(emp_no)==value[0]):
		salary=int(value[3])+int(value[4])+int(value[5])-int(value[6])
		print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<10} {:<10}".format(value[0],value[1],value[2],value[3],value[4],value[5],value[6],salary))
	
file.seek(0)

dept_no=int(input("Enter Dept_no :"))
print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<10}".format("Emp_no","Name","Dept_no","Basic","DA","HRA","Conveyance"))
for line in file:
	value=line.split()
	if(str(dept_no)==value[2]):
		print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<10}".format(value[0],value[1],value[2],value[3],value[4],value[5],value[6]))