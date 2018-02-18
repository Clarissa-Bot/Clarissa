import sys, os
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
		os.mkdir(os.path.expanduser("~")+"/CApps/"+app_name)
		f = open(os.path.expanduser("~")+"/CApps/"+app_name+"/main.py", "w")
		f.write("print(\"This is a sample app\")")
		f.flush()
		f.close()
		print("Sample app stored in "+os.path.expanduser("~")+"/CApps/"+app_name)