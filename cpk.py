import sys, os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("bot", "")

def get_commands():
	if(sys.argv[0] == "cpk.py"):
		sys.argv.remove("cpk.py")
	return sys.argv
def get_beginning_command():
	return get_commands()[0]
def run():
	begin_str = "python bot.py"
	try:
		if(get_beginning_command() == "compile"):
			#Compiles the source code
			os.system("python bot.py "+dir_path+" --build-app "+get_commands()[1])
		elif(get_beginning_command() == "compile" and get_commands()[2] == "--from-external"):
			#Compiles from external source
			os.system("python bot.py "+dir_path+" --build-app "+get_commands()[1] + " --from-external")
		elif(get_beginning_command() == "install"):
			#Installs the built cpk
			os.system"python bot.py "+dir_path+" --install-app "+get_commands()[1])
		elif(get_beginning_command() == "install" and get_commands()[2] == "--from-external"):
			#Installs the built cpk
			os.system(""python bot.py "+dir_path+" --install-app "+get_commands()[1] + " --from-external")
		elif(get_beginning_command() == "make"):
			#Makes a sample app
			os.system("python bot.py "+dir_path+" --make-app "+get_commands()[1])
		elif(get_beginning_command() == "make" and get_commands()[2] == "--javascript"):
			#Installs the built cpk
			os.system("python bot.py "+dir_path+" --make-app "+get_commands()[1] + " --javascript")
		elif(get_beginning_command() == "make" and get_commands()[2] == "--web"):
			#Installs the built cpk
			os.system("python bot.py "+dir_path+" --make-app "+get_commands()[1] + " --web")
		elif(get_beginning_command() == "run"):
			#Runs the app
			os.system("python bot.py "+dir_path+" --run-app "+get_commands()[1])
		elif(get_beginning_command() == "update"):
			#Updates the app
			os.system("python bot.py "+dir_path+" -- build-app "+get_commands()[1])
			os.system("python bot.py "+dir_path+" -- install-app "+get_commands()[1])
	except IndexError as e:
		print("Clarissa Package Manager Help Menu:")
		print("\tcompile: Compiles Clarissa Application to .cpk")
		print("\t\tEx: cpk compile [APP_NAME] (--from-external)")
		print("\tinstall: Installs a Clarissa Package (.cpk) from a directory (optional: --from-external)")
		print("\t\tEx: cpk install [CPK_DIR] (optional: --from-external)")
		print("\tmake: Builds a sample Clarissa Application (--python || --web)")
		print("\t\tEx: cpk make [APP_NAME] (--python || --web)")
		print("\trun: Runs installed app")
		print("\t\tEx: cpk run [APP_NAME]")
		print("\tupdate: Updates installed cpk")
		print("\t\tEx: cpk update [APP_NAME] [optional: --from-external]")
run()
