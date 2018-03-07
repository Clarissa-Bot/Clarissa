import sys
import os
from random import choice
from gtts import gTTS
import tempfile
from playsound import playsound
import shutil
def init(to_speak, language, is_slow):
	print("We are working on improving tts")
	import writer
	writer.setClarissaSetting("main","speak_out", "false")

def play(file,text,lang,slow):
	tts = gTTS(text=text, lang=lang, slow=slow)
	tts.save("Audio/"+file)
	f = tempfile.TemporaryFile()
	tts.write_to_fp(f)
	f.close()
	playsound("Audio/"+file)
	shutil.rmtree("Audio/", True)