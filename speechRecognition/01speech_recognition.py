import speech_recognition as sr

x = True
while x == True :

	r = sr.Recognizer(language = "es-EC", key = "AIzaSyDTaM0l4HpaB_99bWh-tlu30MrAZ6nnEio")
	with sr.Microphone() as source:                # use the default microphone as the audio source
	    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

	try:
	    print("Pruebas Medialab: Acabas de decir " + r.recognize(audio))    # recognize speech using Google Speech Recognition
			
	except LookupError:                            # speech is unintelligible
	    print("Pruebas Medialab: No entendemos tu mensaje")