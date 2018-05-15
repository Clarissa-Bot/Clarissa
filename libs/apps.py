import sys, os
from bot_learn import bot_learn
from zipify.zipify import PAR
from rif import reader
class Apps:
	def __init__(self):
		pass

	def install_app(self,path,app_name):
		p = PAR(path)
		p.depackage()

	def run(self, app_name):
		if(self.does_app_exist(app_name) == True):
			cl_path = str(bot_learn.__file__)
			cl_path = cl_path.replace("\\", "/")
			cl_path = cl_path.replace("bot_learn/", "")
			cl_path = cl_path.replace("bot_learn.py", "")
			cl_path = cl_path.replace("\\", "/")
			app_type = reader.getClarissaSettingWithPath(cl_path+"/Apps/UserApps/"+app_name+"/info.rif", "app", "app_type")
			if(app_type == "python"):
				self.run_python_app(app_name)
			else:
				file = open(cl_path+"/Apps/UserApps/"+app_name+"/app.web", "w")
				file.write("[url] => file:///"+cl_path+"/Apps/UserApps/"+app_name+"/index.html")
				file.flush()
				file.close()
				os.system("java -jar libs/java/SoftyServices.jar Apps/UserApps/"+app_name+"/app.web")
	def run_python_app(self, app_name):
		if(self.does_app_exist(app_name) == True):
			cl_path = str(bot_learn.__file__)
			cl_path = cl_path.replace("\\", "/")
			cl_path = cl_path.replace("bot_learn/", "")
			cl_path = cl_path.replace("bot_learn.py", "")
			cl_path = cl_path.replace("\\", "/")
			sys.path.insert(0, cl_path+"/Apps/UserApps/"+app_name)

			import main as custom_app
			custom_app.main(sys.argv)
	def does_app_exist(self,app_name):
		if(os.path.exists("Apps")):
			if(os.path.exists("Apps/UserApps/"+app_name)):
				return True
			else:
				return False
		else:
			return False

	def make_app(self, app_name):
		if(os.path.exists(os.path.expanduser("~")+"/CApps") is False):
			os.mkdir(os.path.expanduser("~")+"/CApps")
		if(os.path.exists(os.path.expanduser("~")+"/CApps/"+app_name)) is True:
			print("App already exists!")
			exit()
		os.mkdir(os.path.expanduser("~")+"/CApps/"+app_name)
		os.environ[app_name] = (os.path.expanduser("~")+"/CApps/"+app_name)
		cl_path = str(bot_learn.__file__)
		cl_path = cl_path.replace("\\", "/")
		cl_path = cl_path.replace("bot_learn/", "")
		cl_path = cl_path.replace("bot_learn.py", "")
		cl_path = cl_path.replace("\\", "/")
		#Create a .rif file with information about application in it
		f = open(os.path.expanduser("~")+"/CApps/"+app_name+"/info.rif", "w")
		f.write("[name] => "+app_name)
		f.write("\n[app_type] => web")
		#Create the application, then import the requirements
		app_path = os.path.expanduser("~")+"/CApps/"+app_name
		app_path = app_path.replace("\\", "/")
		f = open(app_path+"/index.html", "w")
		f.write("<html>\n\t<header>\n\t\t<title>"+app_name+"</title>\n\t</header>\n\t<body>\n\t</body>\n<html>")
		f.flush()
		f.close()
		#Write javascript file
		f = open(app_path+"/app.js", "w")
		f.write("function getName()\n{\n\treturn \""+app_name+"\";\n}")
		f.flush()
		f.close()
		#Write app file
		f = open(app_path+"/app.web", "w")
		f.write("[url] => file:///"+app_path+"/index.html")
		f.flush()
		f.close()
		#Notify app was created
		print("Sample app stored in "+os.path.expanduser("~")+"/CApps/"+app_name)

	def make_python_app(self, app_name):
		if(os.path.exists(os.path.expanduser("~")+"/CApps") is False):
			os.mkdir(os.path.expanduser("~")+"/CApps")
		if(os.path.exists(os.path.expanduser("~")+"/CApps/"+app_name)) is True:
			print("App already exists!")
			exit()
		os.mkdir(os.path.expanduser("~")+"/CApps/"+app_name)
		os.environ[app_name] = (os.path.expanduser("~")+"/CApps/"+app_name)
		cl_path = str(bot_learn.__file__)
		cl_path = cl_path.replace("\\", "/")
		cl_path = cl_path.replace("bot_learn/", "")
		cl_path = cl_path.replace("bot_learn.py", "")
		cl_path = cl_path.replace("\\", "/")
		#Create a .rif file with information about application in it
		f = open(os.path.expanduser("~")+"/CApps/"+app_name+"/info.rif", "w")
		f.write("[name] => "+app_name)
		f.write("\n[app_type] => python")
		#Create the application, then import the requirements
		app_path = os.path.expanduser("~")+"/CApps/"+app_name
		app_path = app_path.replace("\\", "/")
		f = open(app_path+"/main.py", "w")
		f.write("from app import App\nimport os\ndir_path = os.path.dirname(os.path.realpath(__file__))\napp = App(dir_path)\ndef main(args):\n\tprint(args)\napp.on_exit()")
		f.flush()
		f.close()
		#Write app.py file
		f = open(app_path+"/app.py", "w")
		f.write("def getName():\n\n\treturn \""+app_name+"\"\n")
		f.flush()
		f.close()

		#Get code from App.py
		codes = open("App/App.py", "r").readlines()
		f = open(app_path+"/App.py", "w")
		for code in codes:
			f.write(code)
		f.flush()
		f.close()
		#Notify app was created
		print("Sample app stored in "+os.path.expanduser("~")+"/CApps/"+app_name)