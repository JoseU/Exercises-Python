textTweet = "#ea5 ahi vamos con todo"

# print (textTweet)

messageCheck = ''

x = 0


enterText = input("ingrese su texto: ")
# print (enterText)

while x == 0 :
	
	if enterText != '' :
		
		lengthEText = len(enterText)

		lastSpace =enterText.rfind(' ')
		beginLastWord = lastSpace + 1

		lastWord = enterText[beginLastWord : lengthEText]

		#print (lastWord)

		enterText2 = input("ingrese su texto: ")


		if enterText2.startswith(lastWord) == True :
			#print (enterText2)
			enterText = enterText2
		else :
			print('ERROR! USAR ULTIMA PALABRA')




		
	#if messageCheck