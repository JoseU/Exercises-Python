tweet = input("ingrese su comando: > ")

tweetLower = tweet.lower() #convertir mayus - minus
#print (tweetLower)

findIzq = tweetLower.find('izquierda')
findLeft = tweetLower.find('left')
findDer = tweetLower.find('derecha')
findRight = tweetLower.find('right')
findParar = tweetLower.find('parar')
findStop = tweetLower.find('stop')

if (findIzq + findLeft) != -2 :
	print ('mover hacia la izquierda')

elif (findDer + findRight) != -2 :
	print ('mover hacia la derecha')


elif (findParar + findStop) != -2 :
	print ('parar el funcionamiento')

else :
	print ('no hay instrucción')
