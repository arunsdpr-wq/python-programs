import MySQLdb

conn=MySQLdb.connect(host='localhost',database='python',user='root',password='admin')
cursor=conn.cursor()
cursor.execute("select * from employee")
rows=cursor.fetchall()
print('Total number of rows=',cursor.rowcount)
print("%-3s %-10s %-10s %-6s"%("ID","Name","Designation","Salary"))
for row in rows:
	id=row[0]
	name=row[1]
	designation=row[2]
	salary=row[3]
	print('%-3d %-10s %-10s %-6d'%(id,name,designation,salary))
cursor.close()
conn.close()
