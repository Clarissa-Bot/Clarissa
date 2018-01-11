import sys as sys
import os
os.system("python "+os.environ["USERPROFILE"]+"/._clarissa.py")
false = False
true = True


#Write a file
def write_file(file, message):
	files = open(file, "w")
	files.write(message)
	files.flush()
	files.close()

def delete_file(file):
	os.remove(file)

def getExistingFile(file):
	if(os.path.isfile(file)):
		return true
	else:
		return false

isEngaged = True
def disengage():
	if(isEngaged == true):
		print("Re-engaging...")
		delete_file(".bot_engage")
	else:
		print("You have to engage the bot in order to engage it")
def engage():
	exit()

if(os.path.isfile("bot_response.py") == False):
	file = open("bot_response.py", "w")
	file.write("import logger as log")
	file.write("\ndef getResponse(messageToBot):")
	file.write("\n\tif(\"Hello\" in messageToBot):")
	file.write("\n\t\tprint(\"Clarissa: Hi\")")
	file.write("\n\t\tlog.log(\"chat.log\", \"Clarissa: Hi\")")


if(sys.argv[1] == "engage"):
	engage()
elif ( sys.argv[1] == "disengage" ):
	disengage()
