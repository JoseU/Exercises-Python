from gtts import gTTS

tts = gTTS(text='ahi vamos' , lang='es')

tts.save("hello.mp3")