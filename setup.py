import os
import sys
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import writer as w

def setupClarissa(install_path):
	if(os.path.isfile("setup.ini")):
		out = open('setup.ini', 'a')
		os.system("rm setup.ini")
		del_settings = input("This will delete your current settings. Do you wish to continue? (Y/N)")
		if "y" in del_settings.lower():
			os.system("rm -R Settings")
			os.mkdir("Settings")
		else:
			exit()

	else:
		os.mkdir(install_path+"Settings")
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
	w.setClarissaSetting("speech", "hey_clarissa_enabled", "true")
	w.setClarissaSetting("speech", "speak_out", "true")
	w.setClarissaSetting("main", "user.name", input("Your username: "))


try:
	setupClarissa(sys.argv[1])
except IndexError:
	print("Run python setup.py [CLARISSA_INSTALL_PATH]")