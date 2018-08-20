from logger import logger as log
import urllib.request, urllib.error, urllib.parse
import json
import os as os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("bot_response", "")
import sys as sys
from urllib.request import urlopen
from rif import reader as sr
from tts import tts
from bot_learn import bot_learn as bl
from rif import reader
from rif import writer
from storage import sql_base
from storage.sql_base import SQL

def get_name():
	return reader.getClarissaSetting("clarissa", "name")
cbot_name = ""
cbot_name = get_name()
if(cbot_name is None):
	cbot_name = "Clarissa"

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
	#Communicate with commands.db
	sql = SQL(dir_path+"/commands.db")
	lines = sql.get_results("commands", "response", "`command`=\""+to_bot+"\"")
	for line in lines:
		for line2 in line:
			if(sr.getClarissaSetting("speech", "speak_out") == "true"):
				text = line
				tts.init(text, 'en-US', False)
			print(cbot_name+": "+line2)
			return None
	bl.learn_hobby(to_bot)
movie_lines = dir_path+"/corpus/movie_lines.txt"
movie_convos = dir_path+"/corpus/movie_conversations.txt"

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
	getServerBasedResponse(to_bot)
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
