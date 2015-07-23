import threading, random, time

def Splitter(words) :
	mylist = words.split() # hace una lista de las palabras

	newList = []

	while (mylist) :
		newList.append(mylist.pop (random.randrange(0,len(mylist))))
		print(' '.join(newList))
		time.sleep(0.2)




if __name__ == '__main__':
	sentance = 'I am a handsome beast. Word'
	
	"""while True :

		Splitter(sentance) """




	numOfThreads = 5

	threadList = []

	
	print ("STARTING...\n")

	for i in range(numOfThreads):
		t = threading.Thread(target=Splitter, args=(sentance,))

		t.start()
		threadList.append(t)

	print("\nThread Count: " + str(threading.activeCount()))

	print("EXITING... \n")

	
