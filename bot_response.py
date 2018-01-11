import logger as log
import urllib.request, urllib.error, urllib.parse
import json
import os as os
import sys as sys
from urllib.request import urlopen
import reader as sr
import tts
def getResponse(messageToBot):
	getServerBasedResponse(messageToBot)


def getServerBasedResponse(to_bot):
	url = "http://softy.xyz/apps/sites/clarissa/get.php"
	req = urllib.request.Request(url)
	opener = urllib.request.build_opener()
	file = opener.open(req)
	j = json.loads(file.read())
	text = ""
	for line in range(len(j)):
		if to_bot == j[line]['command']:
			if(sr.getClarissaSetting("speech", "speak_out") == "true"):
				text = j[line]['reply']
				tts.init(text, 'en-UK', False)
			print("Clarissa: "+j[line]['reply'])
		elif to_bot.lower() in j[line]['command'].lower():
			if(sr.getClarissaSetting("speech", "speak_out") == "true"):
				text = j[line]['reply']
				tts.init(text, 'en-UK', False)
			print("Clarissa: "+j[line]['reply'])

	