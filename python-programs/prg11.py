def fibonacci(no):
	if no<=1:
		return 1;
	else:
		temp=fibonacci(no-1)+fibonacci(no-2);
		if temp<num:
			return temp;
		else:
			exit();

num=int(input("Enter number :"));
for i in range(1,num+1):

	print(fibonacci(i));
