import sys, os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("cbot", "")
print(dir_path)

def get_commands():
	sys.argv.remove("cbot.py")
	return sys.argv

def run():
	begin_str = "python "+ dir_path +"/bot.py"
	try:
		comms = get_commands()
		if(comms[0] == "--setup"):
			begin_str = "python "+ dir_path +"/setup.py"
			del comms[0]
		for line in comms:
			begin_str += " " + line
		os.system(begin_str)
	except Exception as e:
		print("Error: "+str(e))
		os.system(begin_str)
run()
