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
import requests
url = 'http://softy.000webhostapp.com/login/login_empty.php'
def download(url, title, path):
	print("Downloading: "+title)
	response = urllib.request.urlopen(url)
	data = response.read()
	text = data
	f = open(path, "wb")
	f.write(text)
	f.flush()
	f.close()
def getStatus(url):
	with open(url, "r") as f:
		j = json.load(f)
	text = ""
	for line in range(len(j)):
		if(j[line]["status"] == "OKAY"):
			w.setClarissaSettingWithPath("user.rif", "user", "user", j[line]["username"])
			w.setClarissaSettingWithPath("user.rif", "pass","pass", j[line]["password"])
		else:
			print("You entered either a wrong username or password")
def useWebServices(ask_in=False):
	if(ask_in is True):
		ask = "Do you wish to sign in? (Y/N) "
	else:
		ask = "Have you signed up for Softy? (Y/N) "
	have_signed_up = input(ask)
	if(have_signed_up == "Y"):
		url = 'http://softy.000webhostapp.com/login/login_empty.php'
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
		writeCommand(user, password,"What is your name?", "My name is Clarissa Campbell!")
		writeCommand(user, password, "What's your name?", "My name is Clarissa Campbell!")
		writeCommand(user, password, "kill-bot", "I had fun chatting!")
	else:
		url = "http://softy.000webhostapp.com/login/register_empty.php"
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
                url = 'http://softy.000webhostapp.com/apps/sites/clarissa/update.php'
                query = {'u': user,
                'p': password,
                'c': command,
                        'r': response,
                        'a': action}
                res = r.post(url, data=query)
                print(res.text)

def setupOfflineClarissa(install_path):
	w.setClarissaSettingWithPath("user.rif", "user", "user", "Offline")
	w.setClarissaSettingWithPath("user.rif", "pass", "pass", "Offline")
	os.remove("setup.rif")
	if(os.path.isfile("setup.rif")):
		out = open('setup.rif', 'a')
		del_settings = input("This will delete your current settings. Do you wish to continue? (Y/N)")
		if "y" in del_settings.lower():
			os.remove("rm -R Settings")
			os.mkdir("Settings")
		else:
			exit()

	else:
		if not os.path.exists(install_path+"/Settings"):
			os.mkdir(install_path+"/Settings")
		out = open('setup.rif', 'w')
	print("Setting up Clarissa. This should not take long.")
	setup = open(os.path.expanduser("~")+"/._clarissa.py", 'w')
	setup.write("import os\n")
	setup.write("os.environ['CLARISSA_PATH']=r\""+install_path+"\"")
	setup.flush()
	setup.close()
	os.environ['CLARISSA_PATH'] = install_path
	w.setClarissaSettingWithPath("setup.rif", "main", "install", install_path)
	w.setClarissaSetting("main", "auto_update", "true")
	w.setClarissaSetting("speech", "hey_clarissa_enabled", "false")
	w.setClarissaSetting("speech", "speak_out", "false")
	w.setClarissaSetting("main", "user.name", input("Your username: "))
	print("Setup successful. When you are back online, re-run this setup.")
def setupClarissa(install_path):
	useWebServices()
	os.remove("setup.rif")
	if(os.path.isfile("setup.rif")):
		out = open('setup.rif', 'a')
		del_settings = input("This will delete your current settings. Do you wish to continue? (Y/N)")
		if "y" in del_settings.lower():
			os.remove("rm -R Settings")
			os.mkdir("Settings")
		else:
			exit()

	else:
		if not os.path.exists(install_path+"/Settings"):
			os.mkdir(install_path+"/Settings")
		out = open('setup.rif', 'w')
	print("Setting up Clarissa. This should not take long.")
	setup = open(os.path.expanduser("~")+"/._clarissa.py", 'w')
	setup.write("import os\n")
	setup.write("os.environ['CLARISSA_PATH']=r\""+install_path+"\"")
	setup.flush()
	setup.close()
	os.environ['CLARISSA_PATH'] = install_path
	w.setClarissaSettingWithPath("setup.rif", "main", "install", install_path)
	w.setClarissaSetting("main", "auto_update", "true")
	w.setClarissaSetting("speech", "hey_clarissa_enabled", "false")
	w.setClarissaSetting("speech", "speak_out", "false")
	w.setClarissaSetting("main", "user.name", input("Your username: "))
	if(os.path.exists("corpus") is False):
		os.mkdir("corpus")
		download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/chameleons.pdf", "Chameleons", "corpus/chameleons.pdf")
		download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/movie_characters_metadata.txt", "Movie Characters Meta Data", "corpus/movie_characters_metadata.txt")
		download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/movie_conversations.txt", "Movie Conversations", "corpus/movie_conversations.txt")
		download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/movie_lines.txt", "Movie Lines", "corpus/movie_lines.txt")
		download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/movie_titles_metadata.txt", "Movie Titles", "corpus/movie_titles_metadata.txt")
		download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/raw_script_urls.txt", "Raw Script", "corpus/raw_script_urls.txt")
		download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/README.txt", "README", "corpus/README.txt")
	if("win32" in sys.platform):
		os.system("python -m pip install -r TO_INSTALL_WINDOWS.txt")
	else:
		os.system("python -m pip install -r TO_INSTALL_LINUX.txt")
def internet_on():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except requests.exceptions.ConnectionError as err: 
        return False
    except urllib.error.URLError as err:
    	return False
try:
	open("setup.rif", "w")
	w.setClarissaSetting("clarissa", "name", "Clarissa")
	if(internet_on() is False):
		setupOfflineClarissa(sys.argv[1])
		exit()
	setupClarissa(sys.argv[1])
except IndexError:
	print("Run python setup.py [CLARISSA_INSTALL_PATH]")
except requests.exceptions.ConnectionError:
	print("Offline setup!")
	setupOfflineClarissa(sys.argv[1])