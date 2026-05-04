str=input("Enter string :");
vowel="aeiouAEIOU";
temp,count=0,0;
for i in str:
	for j in vowel:
		if i==j:
			temp=temp+1;

for i in str:
	count=count+1;

rev=str[::-1];

print("No. of Vowel :",temp);
print("Length of String :",count);
print("Reverse of String :",rev);

if str==rev:
	print("String is palindrome");
else:
	print("String is not palindrome\n");

old=input("Enter old character :");
for i in str:
	if old==i:
		new=input("Enter new character :");
		print(str.replace(old,new));
