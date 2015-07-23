import threading, random, time

def tweetSelector(tweet) :
	tweet_ = tweet # h
	

	if tweet_.find("agua") != -1 :

		print "accionar maquina de agua"

		for x in xrange(1,10):
			print "agua", x
			pass
			time.sleep(0.2)

	elif  tweet_.find("tierra") != -1 :

		print "accionar maquina de tierra"

		for x in xrange(1,10):
			print "tierra", x
			pass
			time.sleep(0.2)



if __name__ == '__main__':
	
	
	while True : 

		consulta = raw_input("digame su tweet: ")

		tweetSelector(consulta)

	"""rampa(10) """

"""
	numOfThreads = 5

	threadList = []

	
	print ("STARTING...\n")

	for i in range(numOfThreads):
		t = threading.Thread(target=rampa, args=(sentance,))

		t.start()
		threadList.append(t)

	print("\nThread Count: " + str(threading.activeCount()))
 
	print("EXITING... \n")  """

	
