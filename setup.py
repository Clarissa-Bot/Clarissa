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
def useWebServices(ask_in=False):
	return "This feature is deprecated"

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

def setupOfflineClarissa():
	w.setClarissaSettingWithPath(dir_path+"/user.rif", "user", "user", "Offline")
	w.setClarissaSettingWithPath(dir_path+"/user.rif", "pass", "pass", "Offline")
	os.remove("setup.rif")
	if(os.path.isfile("setup.rif")):
		out = open('setup.rif', 'a')
		del_settings = input("This will delete your current settings. Do you wish to continue? (Y/N)")
		if "y" in del_settings.lower():
			shutil.rmtree(dir_path + "/Settings")
			os.mkdir(dir_path + "/Settings")
		else:
			exit()

	else:
		if not os.path.exists(dir_path+"/Settings"):
			os.mkdir(dir_path+"/Settings")
		out = open('setup.rif', 'w')
	print("Setting up Clarissa. This should not take long.")
	setup = open(os.path.expanduser("~")+"/._clarissa.py", 'w')
	setup.write("import os\n")
	setup.write("os.environ['CLARISSA_PATH']=r\""+dir_path+"\"")
	setup.flush()
	setup.close()
	os.environ['CLARISSA_PATH'] = dir_path
	w.setClarissaSettingWithPath(dir_path+"/setup.rif", "main", "install", dir_path)
	w.setClarissaSetting("main", "auto_update", "false")
	w.setClarissaSetting("speech", "hey_clarissa_enabled", "false")
	w.setClarissaSetting("speech", "speak_out", "false")
	w.setClarissaSetting("main", "user.name", input("Your username: "))
def setupClarissa():
	useWebServices()
	if(os.path.isfile("setup.rif")):
		out = open('setup.rif', 'a')
		del_settings = input("This will delete your current settings. Do you wish to continue? (Y/N)")
		if "y" in del_settings.lower():
			shutil.rmtree(dir_path + "/Settings")
			os.mkdir(dir_path + "/Settings")
		else:
			exit()

	else:
		if not os.path.exists(dir_path+"/Settings"):
			os.mkdir(dir_path+"/Settings")
		out = open('setup.rif', 'w')
	print("Setting up Clarissa. This should not take long.")
	setup = open(os.path.expanduser("~")+"/._clarissa.py", 'w')
	setup.write("import os\n")
	setup.write("os.environ['CLARISSA_PATH']=r\""+dir_path+"\"")
	setup.flush()
	setup.close()
	os.environ['CLARISSA_PATH'] = dir_path
	w.setClarissaSettingWithPath(dir_path+"/setup.rif", "main", "install", dir_path)
	w.setClarissaSettingWithPath(dir_path+"/setup.rif", "main", "cbot_dir", os.path.dirname(os.path.realpath(__file__)))
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
	if(sys.argv[1] == "--reset"):
		os.remove("commands.list")
		os.remove("setup.rif")
		os.remove("user.rif")
		shutil.rmtree(dir_path + "/Settings")
		shutil.rmtree("Apps")
		exit()
	open(dir_path+"/setup.rif", "w")
	w.setClarissaSetting("clarissa", "name", "Clarissa")
	if(internet_on() is False):
		setupOfflineClarissa()
		exit()
	setupClarissa()
	if("--rebuild-chat" in sys.argv):
		getChat(rewrite_db=True)
except IndexError:
	print("Run python setup.py")
	print("Or python.setup.py [optional:--reset] --rebuild-chat to rebuild chat based on dialogue quotes")
	print("Or run python setup.py --reset to reset Clarissa to default")
except requests.exceptions.ConnectionError:
	print("Offline setup!")
	setupOfflineClarissa()
	if("--rebuild-chat" in sys.argv):
		getChat(rewrite_db=True)
print("Setting up database")
getChat()
print("Done!")
