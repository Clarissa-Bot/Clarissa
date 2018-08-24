from storage import sql_base
from storage.sql_base import SQL
import os as os
#from chatterbot import ChatBot
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("setup", "")
import platform
import bot_response as br
#Install required modules using pip
import pip
import subprocess
def install(package):
	#os.system("pip install -r "+str(package))
	if(float(pip.__version__) >= 10):
		subprocess.check_call(["python", "-m", "pip", "install", package])
	else:
		pip.main(['install', package])
if(platform.system() == "Windows"):
	file = open(dir_path+"/TO_INSTALL_WINDOWS.txt", "r")
	for line in file.readlines():
		install(line)
else:
	file = open(dir_path+"/TO_INSTALL_LINUX.txt", "r")
	for line in file.readlines():
		install(line)
movie_lines = dir_path+"/corpus/movie_lines.txt"
movie_convos = dir_path+"/corpus/movie_conversations.txt"
import sys
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
from rif import writer as w
import requests as r
import urllib.request, urllib.error, urllib.parse
import json
from urllib.request import urlopen
import shutil
import requests
url = 'http://softy.000webhostapp.com/login/login_empty.php'
def clr():
    os.system('cls' if os.name=='nt' else 'clear')
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
			w.setClarissaSettingWithPath(dir_path+"/user.rif", "user", "user", j[line]["username"])
			w.setClarissaSettingWithPath(dir_path+"/user.rif", "pass","pass", j[line]["password"])
		else:
			print("You entered either a wrong username or password")
def useWebServices(ask_in=False):
	return "This feature was removed"

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
	w.setClarissaSettingWithPath(dir_path+"/user.rif", "user", "user", "Offline")
	w.setClarissaSettingWithPath(dir_path+"/user.rif", "pass", "pass", "Offline")
	if(os.path.isfile(dir_path+"/settings.rif")):
		out = open('settings.rif', 'a')
		del_settings = input("This will delete your current settings. Do you wish to continue? (Y/N)")
		if "y" in del_settings.lower():
			shutil.rmtree("Settings")
			os.mkdir("Settings")
		else:
			exit()

	else:
		if not os.path.exists(install_path+"/Settings"):
			os.mkdir(install_path+"/Settings")
		out = open('settings.rif', 'w')
	print("Setting up Clarissa. This should not take long.")
	setup = open(os.path.expanduser("~")+"/._clarissa.py", 'w')
	setup.write("import os\n")
	setup.write("os.environ['CLARISSA_PATH']=r\""+install_path+"\"")
	setup.flush()
	setup.close()
	os.environ['CLARISSA_PATH'] = install_path
	w.setClarissaSettingWithPath(dir_path+"/settings.rif", "main", "install", install_path)
	w.setClarissaSetting("main", "auto_update", "false")
	w.setClarissaSetting("speech", "hey_clarissa_enabled", "false")
	w.setClarissaSetting("speech", "speak_out", "false")
	w.setClarissaSetting("main", "user.name", input("Your username: "))
	print("Setup successful. When you are back online, re-run this setup.")
def setupClarissa(install_path):
	useWebServices()
	os.remove(dir_path+"/settings.rif")
	if(os.path.isfile(dir_path+"/settings.rif")):
		out = open('settings.rif', 'a')
		del_settings = input("This will delete your current settings. Do you wish to continue? (Y/N)")
		if "y" in del_settings.lower():
			os.remove("rm -R Settings")
			os.mkdir("Settings")
		else:
			exit()

	else:
		if not os.path.exists(install_path+"/Settings"):
			os.mkdir(install_path+"/Settings")
		out = open('settings.rif', 'w')
	print("Setting up Clarissa. This should not take long.")
	setup = open(os.path.expanduser("~")+"/._clarissa.py", 'w')
	setup.write("import os\n")
	setup.write("os.environ['CLARISSA_PATH']=r\""+install_path+"\"")
	setup.flush()
	setup.close()
	os.environ['CLARISSA_PATH'] = install_path
	w.setClarissaSettingWithPath(dir_path+"/settings.rif", "main", "install", install_path)
	w.setClarissaSettingWithPath(dir_path+"/settings.rif", "main", "cbot_dir", os.path.dirname(os.path.realpath(__file__)))
	w.setClarissaSetting("main", "auto_update", "false")
	w.setClarissaSetting("speech", "hey_clarissa_enabled", "false")
	w.setClarissaSetting("speech", "speak_out", "false")
	w.setClarissaSetting("main", "user.name", input("Your username: "))
	w.setClarissaSetting("clarissa", "name", "Clarissa")
	if(os.path.exists(dir_path+"/corpus") is False):
		os.mkdir("corpus")
		download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/chameleons.pdf", "Chameleons", dir_path+"/corpus/chameleons.pdf")
		download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/movie_characters_metadata.txt", "Movie Characters Meta Data", dir_path+"/corpus/movie_characters_metadata.txt")
		download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/movie_conversations.txt", "Movie Conversations", dir_path+"/corpus/movie_conversations.txt")
		download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/movie_lines.txt", "Movie Lines", dir_path+"/corpus/movie_lines.txt")
		download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/movie_titles_metadata.txt", "Movie Titles", dir_path+"/corpus/movie_titles_metadata.txt")
		download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/raw_script_urls.txt", "Raw Script", dir_path+"/corpus/raw_script_urls.txt")
		download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/README.txt", "README", dir_path+"/corpus/README.txt")


def internet_on():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except requests.exceptions.ConnectionError as err: 
        return False
    except urllib.error.URLError as err:
    	return False


def _sql(path, commands):
	sql = SQL(path)
	sql.use_commands(commands)
	sql.finalize()
def get_id2line():

    lines=open(movie_lines,encoding = "ISO-8859-1").read().split('\n')

    id2line = {}

    for line in lines:

        _line = line.split(' +++$+++ ')

        if len(_line) == 5:

            id2line[_line[0]] = _line[4]
    return id2line

def getChat(rewrite_db=False):
	if(rewrite_db == True):
			#Create the commands.db file
			sql = SQL("commands.db")
			#Write the commands table to it if it does not exist
			sql.use_commands("CREATE TABLE IF NOT EXISTS commands(command VARCHAR(65535), response VARCHAR(65535))")
			#Return convos
			convs = getConvos()
			#Return id2line
			id2line = get_id2line()
			a = ""
			used_line = [ ]
			num_indexed = 0
			to_index = len(convs)

			#Index all possible commands and responses
			#To database
			to_index = 83097
			for conv in convs:
				if len(conv) %2 != 0:
					conv = conv[:-1]
				for i in range(len(conv)):
					try:
						#Index number of times
						#We have been running
						num_indexed += 1
						#Default check if num_index > 1000
						if (sys.argv[2] == "--max-index"):
							if(num_indexed > int(sys.argv[3])):
								return None
						#Clear the view
						clr()
						if(int(sys.argv[3]) > 0):
							to_index = int(sys.argv[3])
						else:
							to_index = 83097
						print("Possible index of %s out of %s"%(num_indexed, to_index))
						if i%2 == 0:
							sql.use_commands('''INSERT INTO commands(command, response) VALUES("%s", "%s")'''%(id2line[conv[i]],id2line[conv[i+1]]))
							sql.finalize()
					except IndexError as e:
						clr()
						to_index = 83097
						print("Possible index of %s out of %s"%(num_indexed, to_index))
						if i%2 == 0:
							sql.use_commands('''INSERT INTO commands(command, response) VALUES("%s", "%s")'''%(id2line[conv[i]],id2line[conv[i+1]]))
							sql.finalize()
			sql.use_commands('''INSERT INTO commands(command, response) VALUES("kill-bot", "Thank you for using Clarissa")''')
			sql.finalize()
			return sql
	print("Using existing commands database")

def getConvos():
	lines = open(movie_convos,encoding = "ISO-8859-1").read().split("\n")
	convs = [ ]
	for line in lines[:-1]:
		_line = line.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
		convs.append(_line.split(','))

	return convs

try:
	open(dir_path+"/settings.rif", "w")
	
	if(sys.argv[1] == "--reset"):
		os.remove("commands.list")
		exit()
	if(internet_on() is False):
		setupOfflineClarissa(dir_path)
		exit()
	setupClarissa(dir_path)
	if(sys.argv[1] == "--set-bot-name"):
		w.setClarissaSetting("clarissa", "name", sys.argv[2])
	else:
		w.setClarissaSetting("clarissa", "name", "Clarissa")
except IndexError:
	print("Run python setup.py")
	print("Or run python setup.py --reset to reset Clarissa to default")
	print("Or run python setup.py --rebuild-chat to rebuild the chat database")
	print("Or run python setup.py --set-bot-name [BOT_NAME] to change Clarissa's name")
	if(internet_on() is False):
		setupOfflineClarissa(dir_path)
		exit()
	setupClarissa(dir_path)
except requests.exceptions.ConnectionError:
	print("Offline setup!")
	setupOfflineClarissa(dir_path)
	if(sys.argv[1] is "--set-bot-name"):
		w.setClarissaSetting("clarissa", "name", sys.argv[2])
	else:
		w.setClarissaSetting("clarissa", "name", "Clarissa")
print("Setting up database")
getChat()
print("Done!")
