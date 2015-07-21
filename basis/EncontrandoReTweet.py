counterRT = 0 # Para contar los retweets

while True:

	tweet = raw_input ('send mi a tweet: ')
	rtIn = tweet.startswith( 'RT' )
	# print rtIn
	if rtIn == True :
		counter = counter + 1
		print counter
	elif tweet == "quit" :
		break;


