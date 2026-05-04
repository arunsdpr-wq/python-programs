import MySQLdb

conn=MySQLdb.connect(host='localhost',database='python',user='root',password='admin')
cursor=conn.cursor()
cursor.execute("select * from employee")
rows=cursor.fetchone()
f=open("prg4.csv","w")
while rows is not None:
	f.write(str(rows))
	f.write('\n')
	rows=cursor.fetchone()
