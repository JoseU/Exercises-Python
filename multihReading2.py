import threading, random, time

def rampa(tempo) :
	tempoFinal = tempo # h
	
	count = 0


	while (tempo) :

		count = count + 1
		print "count: ", count

		if count == tempoFinal :
			break

		time.sleep(0.2)




if __name__ == '__main__':
	sentance = 20
	
	"""while True : """

	"""rampa(10) """


	numOfThreads = 5

	threadList = []

	
	print ("STARTING...\n")

	for i in range(numOfThreads):
		t = threading.Thread(target=rampa, args=(sentance,))

		t.start()
		threadList.append(t)

	print("\nThread Count: " + str(threading.activeCount()))
 
	print("EXITING... \n") 

	
