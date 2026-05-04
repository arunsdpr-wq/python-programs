import MySQLdb
import pandas as pd

f=pd.read_csv("emp.csv")
c1=dict(f[['id','name','designation','salary']])
print(f)
for line in f:
	print(line)
	c1[id]=line[0]
	name=line[1]
	designation=line[2]
	salary=line[3]

conn=MySQLdb.connect(host='localhost',database='python',user='root',password='admin')
cursor=conn.cursor()
str="insert into employee values(%d,'%s','%s',%d)"
args=(c1['id'],c1['name'],c1['designation'],c1['salary'])
cursor.execute(str % args)
conn.commit()