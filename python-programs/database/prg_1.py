import MySQLdb

while True:
	print('1-Add Record')
	print('2-Modify Record')
	print('3-Display Record')
	print('4-Delete Record')
	ch=int(input('Enter choice:'))
	conn=MySQLdb.connect(host='localhost',database='python',user='root',password='admin')
	cursor=conn.cursor()

	if ch==1:
		str="insert into employee values(%d,'%s','%s',%d)"
		id=int(input('Enter ID: '))
		name=input('Enter Name: ')
		designation=input('Enter Designation: ')
		salary=int(input('Enter Salary: '))
		args=(id,name,designation,salary)
		cursor.execute(str % args)
		conn.commit()
		print("\nRow inserted\n")
	elif ch==2:
		str="update employee set salary=salary+1000 where id='%d'"
		sal=int(input('Enter ID where you want to update salary: '))
		args=(sal)
		cursor.execute(str % args)
		conn.commit()
		print("\nRecord Modified\n")
	elif ch==3:
		str="select * from employee"
		cursor.execute(str)
		row=cursor.fetchone()
		while row is not None:
			print("\n",row)
			row=cursor.fetchone()
	elif ch==4:
		str="delete from employee where id=%d"
		id=int(input('Enter ID for deletion: '))
		args=(id)
		cursor.execute(str % args)
		conn.commit()
		print("\nRecord Deleted\n")
	else:
		break;
cursor.close()
conn.close()