
for i in range(10):
	numbers = [int(input('Enter 10 value: '))]	

maxx=0;
for i in numbers:
	if i%2!=0:
		if i>maxx:
			maxx=i;
if maxx==0:
	print("No odd numbers");
else:
	print(maxx);