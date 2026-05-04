import socket
host=input('Enter Website :')
try:
	addr=socket.gethostbyname(host)
	print('IP address='+addr)
except Exception as e:
	print('The website does not exist')
