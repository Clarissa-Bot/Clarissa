from logger import logger as log
import urllib.request, urllib.error, urllib.parse
import json
import os as os
import sys as sys
from urllib.request import urlopen
from rif import reader as sr
from tts import tts
from bot_learn import bot_learn as bl
from rif import reader
from rif import writer

def get_name():
	return reader.getClarissaSetting("clarissa", "name")

cbot_name = get_name()

def set_name(bot_name):
	writer.setClarissaSetting("clarissa", "name", bot_name)
	#import bot as bot
	os.system("py -3 "+str("bot.py"))

def getResponse(messageToBot):
	import requests
	try:
		getServerBasedResponse(messageToBot)
	except urllib.error.HTTPError:
		getChatBasedResponse(messageToBot)
	except requests.exceptions.ConnectionError:
		getChatBasedResponse(messageToBot)
	except:
		getChatBasedResponse(messageToBot)

def getServerBasedResponse(to_bot):
	#Use chatterbot to come up with response
	#Then add response to server if command is not on server
	t = ""
	import requests
	url = "http://softy.xyz/apps/sites/clarissa/get.php"
	query = {'user': reader.getClarissaSettingWithPath('user.rif', 'user', 'user'),
	'pass': reader.getClarissaSettingWithPath('user.rif', 'pass', 'pass')
	}
	res = requests.post(url,data=query)
	j = json.loads(res.text)
	text = ""
	for line in range(len(j)):
		if to_bot == j[line]['command']:
			if(sr.getClarissaSetting("speech", "speak_out") == "true"):
				text = j[line]['reply']
				tts.init(text, 'en-US', False)
			print(cbot_name+": "+j[line]['reply'])
			return None
		elif to_bot.lower() in j[line]['command'].lower():
			if(sr.getClarissaSetting("speech", "speak_out") == "true"):
				text = j[line]['reply']
				tts.init(text, 'en-US', False)
			print(cbot_name+": "+j[line]['reply'])
			return None
	t = text
	if(sr.getClarissaSetting("speech", "speak_out") == "true"):
		text = getChat(to_bot)
		tts.init(text, 'en-US', False)
	if(getChat(to_bot) is not ""):
		print(cbot_name+": "+getChat(to_bot))
	import requests as r
	url = 'http://softy.xyz/apps/sites/clarissa/update.php'
	#Learn hobby
	t = bl.learn_hobby(to_bot)
	if( t == ""):
		return None
	if(sr.getClarissaSetting("speech", "speak_out") == "true"):
		text = t
		tts.init(text, 'en-US', False)
	#We must know if getChat response is empty for some reason
	if ( getChat(to_bot) is ""):
		return None
	query = {
	'u' : sr.getClarissaSettingWithPath("user.rif", "user", "user"),
	'p' : sr.getClarissaSettingWithPath("user.rif", "pass", "pass"),
	'c': to_bot,
			'r': t,
			'a': "None"}
	t = getChat(to_bot)
	query = {
	'u' : sr.getClarissaSettingWithPath("user.rif", "user", "user"),
	'p' : sr.getClarissaSettingWithPath("user.rif", "pass", "pass"),
	'c': to_bot,
			'r': t,
			'a': "None"}
	res = r.post(url, data=query)


movie_lines = "corpus/movie_lines.txt"
movie_convos = "corpus/movie_conversations.txt"

def getConvos():
	lines = open(movie_convos,encoding = "ISO-8859-1").read().split("\n")
	convs = [ ]
	for line in lines[:-1]:
		_line = line.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
		convs.append(_line.split(','))

	return convs

def get_id2line():

    lines=open(movie_lines,encoding = "ISO-8859-1").read().split('\n')

    id2line = {}

    for line in lines:

        _line = line.split(' +++$+++ ')

        if len(_line) == 5:

            id2line[_line[0]] = _line[4]

    return id2line
def getChatBasedResponse(to_bot):
	print(cbot_name+": "+getChat(to_bot))
	bl.learn_hobby(to_bot)
def getChat(to_bot):
	question = to_bot
	convs = getConvos()
	id2line = get_id2line()
	a = ""
	used_line = [ ]
	for conv in convs:
		if len(conv) %2 != 0:
			conv = conv[:-1]
		for i in range(len(conv)):
			if i%2 == 0:
				if(question == id2line[conv[i]]):
					a = id2line[conv[i+1]]
				elif(id2line[conv[i]].lower() == question.lower()):
					a = id2line[conv[i+1]]
	return a