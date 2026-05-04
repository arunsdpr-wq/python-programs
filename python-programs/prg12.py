def factorial(no):
    if no == 0:
        return 1;
    else:
        return no * factorial(no-1);

num=int(input("Enter number :"));
for i in range(1,num+1):
	print("Factorial of ",i," is ",factorial(i));
