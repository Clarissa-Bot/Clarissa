import sys, os
import bot_learn
class Apps:
	def __init__(self):
		pass

	def install_app(self,path,app_name):
		print("Installing!")
		if(os.path.exists(os.path.expanduser("~")+"/CApps") is False):
			os.mkdir(os.path.expanduser("~")+"/CApps")
		with zipfile.ZipFile(path, 'r') as zipr:
			zipr.extractall(os.path.expanduser("~")+"/CApps/"+app_name)
		print("Done!")

	def run(self, app_name):
		if(self.does_app_exist(app_name) == True):
			os.system(os.path.expanduser("~")+"/CApps/"+app_name+"/main.py")

	def does_app_exist(self,app_name):
		if(os.path.expanduser("~")+"/CApps"):
			if(os.path.exists(os.path.expanduser("~")+"/CApps/"+app_name)):
				return True
			else:
				return False
		else:
			return False

	def make_app(self, app_name):
		if(os.path.exists(os.path.expanduser("~")+"/CApps") is False):
			os.mkdir(os.path.exists(os.path.expanduser("~")+"/CApps"))
		os.mkdir(os.path.expanduser("~")+"/CApps/"+app_name)
		cl_path = str(bot_learn.__file__)
		cl_path = cl_path.replace("\\", "/")
		cl_path = cl_path.replace("bot_learn.py", "")
		#Create a .rif file with information about application in it
		f = open(os.path.expanduser("~")+"/CApps/"+app_name+"/info.rif", "w")
		f.write("[name] => "+app_name)
		#Create the appinfo module, a requirement to import Clarissa
		#Then write the cl_path to it
		f = open(os.path.expanduser("~")+"/CApps/"+app_name+"/appinfo.py", "w")
		f.write("import sys\nsys.path.insert(0, \""+cl_path+"\")")
		#Create the application, then import the requirements
		f = open(os.path.expanduser("~")+"/CApps/"+app_name+"/main.py", "w")
		f.write("import sys\nimport os\nimport appinfo\nfrom App import App\napp = App(os.path.dirname(os.path.realpath(__file__)))\n")
		f.write("def main(args=sys.argv):\n\tprint(app.get_name())\nmain()")
		f.flush()
		f.close()
		#Notify app was created
		print("Sample app stored in "+os.path.expanduser("~")+"/CApps/"+app_name)