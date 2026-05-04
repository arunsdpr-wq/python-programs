from threading import *
from time import *
class railway:
	def __init__(self,available):
		self.available=available
		self.l=Lock()
	def reserve(self,wanted):
		self.l.acquire()
		print('available no. of berths= ',self.available)

		if self.available>=wanted:
			name=current_thread().getName()
			print('%d berths allotted for %s'%(wanted,name))
			sleep(1.5)
			self.available-=wanted
		else:
			print('No berths')
		self.l.release()
obj=railway(1)
t1=Thread(target=obj.reserve,args=(1,))
t2=Thread(target=obj.reserve,args=(1,))

t1.setName('First')
t2.setName('Second')

t1.start()
t2.start()