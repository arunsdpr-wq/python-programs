class Bank:
	def __init__(self):
		self.acc_no=0
		self.bal=0
		print(self.bal)
	def addbank(self):
		self.acc_no=int(input("Enter the Bank Account Number :"))
	def deposit(self):
		amt=int(input("Enter Amount for Deposit :"))
		self.bal=self.bal+amt
		print("Amount Deposited!")
	def withdraw(self):
		amt=int(input("Enter Amount for Withdraw :"))
		self.bal=self.bal-amt
		print("\nAmount Withdrawed!")		
	def transfer(self):
		print("transfer")
	def balance(self):
		print("Total Balance :",self.bal)

b=Bank()
ch=-1;
while(ch!=0):
    print("1 - Add Bank Accoount")
    print("2 - Deposit Money")
    print("3 - Withdraw Money")
    print("4 - transfer")
    print("5 - Show balance")
    print("0 - Exit")
    ch=int(input("Enter your Choice :"))
    if(ch==1):
        b.addbank()
    if(ch==2):
       	b.deposit()
    if(ch==3):
        b.withdraw()
    if(ch==4):
    	b.transfer()
    if(ch==5):
    	b.balance()



