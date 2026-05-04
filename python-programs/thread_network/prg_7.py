import socket
host='127.0.0.1'
port=9000

s=socket.socket()
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print("A client connected")
while True:
	data=c.recv(1024)
	if not data:
		break
	print("From client: "+str(data.decode()))
	data1=input("Enter response: ")
	c.send(data1.encode())
c.close()