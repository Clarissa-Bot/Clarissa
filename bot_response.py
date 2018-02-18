from chatterbot import ChatBot
from chatterbot.conversation import Statement
import logger as log
import urllib.request, urllib.error, urllib.parse
import json
import os as os
import sys as sys
from urllib.request import urlopen
import reader as sr
import tts
def getResponse(messageToBot):
	try:
		getServerBasedResponse(messageToBot)
	except urllib.error.HTTPError:
		getChatBasedResponse(messageToBot)

def getServerBasedResponse(to_bot):
	#Use chatterbot to come up with response
	#Then add response to server if command is not on server
	cb = ChatBot('Clarissa', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
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
				tts.init(text, 'en-US', False)
			print("Clarissa: "+j[line]['reply'])
			return None
		elif to_bot.lower() in j[line]['command'].lower():
			if(sr.getClarissaSetting("speech", "speak_out") == "true"):
				text = j[line]['reply']
				tts.init(text, 'en-US', False)
			print("Clarissa: "+j[line]['reply'])
			return None
	
	if(sr.getClarissaSetting("speech", "speak_out") == "true"):
		text = str(Statement(cb.get_response(to_bot)))
		tts.init(text, 'en-US', False)
	import requests as r
	url = 'http://softy.xyz/apps/sites/clarissa/update.php'
	query = {'c': to_bot,
			'r': str(Statement(cb.get_response(to_bot))),
			'a': "None"}
	res = r.post(url, data=query)
	print("Clarissa: "+str(Statement(cb.get_response(to_bot))))

def getChatBasedResponse(to_bot):
	#Get raw chat based response
	cb = ChatBot('Clarissa', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
	print("Clarissa: "+str(Statement(cb.get_response(to_bot))))