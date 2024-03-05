from gtts import gTTS

my_first_sound = gTTS('hello teacher, how is my app', lang='en')
my_first_sound.save('hello.mp3')

