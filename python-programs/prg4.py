def addition():
	add=num1+num2;
	print("Addition :",add);

def subtraction():
	sub=num1-num2;
	print("Subtraction :",sub);

def multiplication():
	mul=num1*num2;
	print("Multiplication :",mul);

def division():
	div=num1/num2;
	print("Division :",div);


print("Select Operation ");
print("1-Addition");
print("2-Subtraction");
print("3-Multiplication");
print("4-Division");

choice=int(input("Enter choice :"));

num1=int(input("Enter 1st number :"));
num2=int(input("Enter 2nd number :"));

if choice==1:
	addition();
elif choice==2:
	subtraction();
elif choice==3:
	multiplication();
elif choice==4:
	division();