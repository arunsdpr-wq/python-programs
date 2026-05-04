num=int(input("Enter number :"));
no=num;
temp,rem=0,0;
while num>0:
	rem=num%10;
	temp=temp+(rem*rem*rem);
	num=int(num/10);

print(temp)
if no==temp:
	print("Number is armstrong");
else:
	print("Number is not armstrong");