from chatterbot import ChatBot
import os
import sys
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import writer as w
import requests as r
import urllib.request, urllib.error, urllib.parse
import json
from urllib.request import urlopen
url = 'http://softy.xyz/login/login_empty.php'
def download(url, title):
	print("Downloading: "+title)
	response = urllib.request.urlopen(url)
	data = response.read()
	text = data.decode('utf-8')
	print(text)
def getStatus(url):
	with open(url, "r") as f:
		j = json.load(f)
	text = ""
	for line in range(len(j)):
		if(j[line]["status"] == "OKAY"):
			w.setClarissaSettingWithPath("user.ini", "user", "user", j[line]["username"])
			w.setClarissaSettingWithPath("user.ini", "pass","pass", j[line]["password"])
		else:
			print("You entered either a wrong username or password")
def useWebServices(ask_in=False):
	if(ask_in is True):
		ask = "Do you wish to sign in or register again? (Y/N) "
	else:
		ask = "Have you signed up for Softy? (Y/N) "
	have_signed_up = input(ask)
	if(have_signed_up == "Y"):
		url = 'http://softy.xyz/login/login_empty.php'
		user = input("Username: ")
		password = input("Password: ")
		query = {"username": user,
		"password": password,
		"go": ""}
		res = r.post(url, data=query)
		f = open("user.json","w")
		f.write(res.text)
		f.flush()
		f.close()
		getStatus("user.json")
		os.remove("user.json")
	else:
		url = "http://softy.xyz/login/register_empty.php"
		pn = input("Phone number: ")
		em = input("Email: ")
		user = input("Username: ")
		password = input("Password: ")
		query = {
		"number": pn,
		"email": em,
		"username": user,
		"password": password,
		"go": ""
		}
		res = r.post(url, data=query)
		writeCommand(user, password,"What is your name?", "My name is Clarissa Campbell!")
		writeCommand(user, password, "What's your name?", "My name is Clarissa Campbell!")
		writeCommand(user, password, "kill-bot", "I had fun chatting!")
		useWebServices(ask_in=True)

def writeCommand(user, password, command, response):
        commandList = open("commands.list", "w")
        commandList.write(command)
        commandList.flush()
        commandList.close()
        action = "None"
        if "Y" in "Y":
                import requests as r
                url = 'http://softy.xyz/apps/sites/clarissa/update.php'
                query = {'u': user,
                'p': password,
                'c': command,
                        'r': response,
                        'a': action}
                res = r.post(url, data=query)
                print(res.text)

def setupClarissa(install_path):
	useWebServices()
	os.remove("setup.ini")
	if(os.path.isfile("setup.ini")):
		out = open('setup.ini', 'a')
		del_settings = input("This will delete your current settings. Do you wish to continue? (Y/N)")
		if "y" in del_settings.lower():
			os.remove("rm -R Settings")
			os.mkdir("Settings")
		else:
			exit()

	else:
		if not os.path.exists(install_path+"/Settings"):
			os.mkdir(install_path+"/Settings")
		out = open('setup.ini', 'w')
	print("Setting up Clarissa. This should not take long.")
	setup = open(os.environ['USERPROFILE']+"/._clarissa.py", 'w')
	setup.write("import os\n")
	setup.write("os.environ['CLARISSA_PATH']=r\""+install_path+"\"")
	setup.flush()
	setup.close()
	os.environ['CLARISSA_PATH'] = install_path
	w.setClarissaSettingWithPath("setup.ini", "main", "install", install_path)
	w.setClarissaSetting("main", "auto_update", "true")
	w.setClarissaSetting("speech", "hey_clarissa_enabled", "false")
	w.setClarissaSetting("speech", "speak_out", "false")
	w.setClarissaSetting("main", "user.name", input("Your username: "))
	if(os.path.exists("corpus") is True):
		download("https://www.softy.xyz/apps/sites/clarissa/chameleons.pdf", "Chameleons")
		download("https://www.softy.xyz/apps/sites/clarissa/movie_characters_metadata.txt", "Movie Characters Meta Data")
		download("https://www.softy.xyz/apps/sites/clarissa/movie_conversations.txt", "Movie Conversations")
		download("https://www.softy.xyz/apps/sites/clarissa/movie_lines.txt", "Movie Lines")
		download("https://www.softy.xyz/apps/sites/clarissa/movie_titles_metadata.txt", "Movie Titles")
		download("https://www.softy.xyz/apps/sites/clarissa/raw_script_urls.txt", "Raw Script")
		download("https://www.softy.xyz/apps/sites/clarissa/README.txt", "README")
	os.system("pip install -r TO_INSTALL.txt")
	
try:
	setupClarissa(sys.argv[1])
except IndexError:
	print("Run python setup.py [CLARISSA_INSTALL_PATH]")