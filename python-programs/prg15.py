import os.path
import random

class reserve:
        
    def reserveticket(self):
        li=[]
        file=open("prg15.txt",'a')
        name=input("Input your name :")
        date=input("Enter the date dd/mm/yy format :")
        start=input("Enter the start city :")
        end=input("Enter the end city :")
        pnr=str(random.randint(1000000000,20000000000))
        li.append(name)
        li.append(date)
        li.append(start)
        li.append(end)
        li.append(pnr)
        for line in li:
            file.write(str(line)+" ")
        file.write("\n")
        file.close()

    def get_ticket(self):
        file=open("prg15.txt",'r')
        dat=input("Enter today date :")
        data=[]
        data=file.readlines() 
        print("Details".center(50,"#"))
        print("\n{:10} {:10} {:10} {:10} {:10}".format("Name","Date","Start","End","PNR"))
        for line in data:
                value=line.split()
                if dat==value[1]:
                    for i in value:
                        print(i.ljust(10),end="")
                    print("\n")
        
"""        
if os.path.isfile("prg15.txt"):
    print("File already exist")
else:
    file=open("prg15.txt","w")
"""
ch=-1
while(ch!=0):
    print("1 - Booking ticket\n2 - Information of todays ticket\n0 - Exit\n")
    ch=int(input("Enter choice :"))
    r=reserve()
    if(ch==1):
        r.reserveticket()
    elif(ch==2):
        r.get_ticket()
    elif(ch==3):
        sys.Exit()