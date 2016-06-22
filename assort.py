import _thread
import time

def assort(N):
	time.sleep(N/2) #lemme sleep
	print(N)

try:
	N=[int(i) for i in input().split()]
	for i in N :
		_thread.start_new_thread( assort, (i, ) )
except:
	print ("Hoo u suck")
while 1:
	pass


'''	God who art in Heaven, forgive my stupidity :( '''
