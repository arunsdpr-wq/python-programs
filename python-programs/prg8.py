num=int(input("Enter number :"));
no=num;
res=0;
while num>0:
	temp=num%10;
	res=(res*10)+temp;
	num=int(num/10);

if(no==res):
	print("Number is Palindrome");
else:
	print("Number is not Palindrome");