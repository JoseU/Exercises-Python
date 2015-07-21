import pyglet.media as media
from gtts import gTTS
import time

tts = gTTS(text='como pongo play' , lang='es')

tts.save("hello.mp3")

time.sleep(4)


fname='hello.mp3'
src=media.load(fname)
player=media.Player()
player.queue(src)
player.volume=1.0
player.play()