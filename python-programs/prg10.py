def histogram(num):
	for i in num:
		print("x"*i);


numbers=[];
end=int(input("Enter length of list :"));
for i in range(end):
	num=int(input("Enter value :"));
	numbers.append(num);
print(numbers);	
histogram(numbers);

