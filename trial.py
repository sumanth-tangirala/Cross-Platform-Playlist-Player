import threading,time


def trial():
	for a in range(10):
		print('Sleeping')
		time.sleep(5)
		print('Just slept')

def trial2():
	t = threading.Thread(target = trial())
	t.start()
	print('Heya')

trial2()
