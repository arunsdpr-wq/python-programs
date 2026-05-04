num1=10;
num2=20;

print("Before Swapping :");
print("Number 1 :",num1);
print("Number 2 :",num2);

num1=num1 ^ num2;
num2=num1 ^ num2;
num1=num1 ^ num2;

print("After Swapping :");
print("Number 1 :",num1);
print("Number 2 :",num2);