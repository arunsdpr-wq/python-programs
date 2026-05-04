import os.path
from datetime import date

class library:
        
    def issue_book(self):
        li=[]
        file=open("prg16.txt",'a')
        name=input("Enter Student name :")
        dat=input("Enter date(dd/mm/yy) :")
        book_id=input("Enter Book ID :")
        book_name=input("Enter Book name :")
        
        li.append(name)
        li.append(dat)
        li.append(book_id)
        li.append(book_name)
        for line in li:
            file.write(str(line)+" ")
        file.write("\n")
        file.close()

    def get_info(self):
        file=open("prg16.txt",'r')
        dat=date.today().strftime("%d/%m/%y")
        data=[]
        data=file.readlines() 
        print("Details".center(50,"#"))
        print("\n{:15} {:10} {:15} {:10}".format("Student_Name","Date","Book_id","Book_name"))
        for line in data:
            value=line.split()
            if dat==value[1]:
                for i in value:
                    print(i.ljust(15),end="")
                print("\n",end="")
        
ch=-1
while(ch!=0):
    print("1 - Issue Book\n2 - Information today's issued book\n0 - Exit\n")
    ch=int(input("Enter choice :"))
    l=library()
    if(ch==1):
        l.issue_book()
    elif(ch==2):
        l.get_info()
    elif(ch==3):
        sys.Exit()