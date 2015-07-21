import pyglet

player = pyglet.media.Player()

player.queue("/Users/cottonmouth/Desktop/PYTHON\ PRUEBAS\ EA/audioPython/hearBeat.wav")
player.play()

"""while True: 

	consulta = input('Que deseas 1 play 2 parar: ')

	if consulta == 0: 
		music.play()
		pyglet.app.run()
	elif consulta == 1:
		music.pause()
		pyglet.app.run()"""