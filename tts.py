import sys
import os
from random import choice
from gtts import gTTS
import tempfile
from playsound import playsound
import shutil
def init(to_speak, language, is_slow):
	if(os.path.isdir('Audio') == False):
		os.mkdir("Audio")
	file_name = ''.join([choice("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in range(5)])
	file_name = file_name+".mp3"
	text = to_speak
	lang = language
	slow = is_slow
	play(file_name, to_speak, language, is_slow)

def play(file,text,lang,slow):
	tts = gTTS(text=text, lang=lang, slow=slow)
	tts.save("Audio/"+file)
	f = tempfile.TemporaryFile()
	tts.write_to_fp(f)
	f.close()
	playsound("Audio/"+file)
	shutil.rmtree("Audio/", True)