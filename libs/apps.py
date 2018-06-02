import sys, os
from bot_learn import bot_learn
from zipify.zipify import PAR
from rif import reader
import webview as webview
import platform
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
			name = reader.getClarissaSettingWithPath(cl_path+"/Apps/UserApps/"+app_name+"/info.rif", "app", "name")
			if(app_type == "python"):
				self.run_python_app(app_name)
			else:
				file = open(cl_path+"/Apps/UserApps/"+app_name+"/app.web", "w")
				file.write("[url] => file:///"+cl_path+"Apps/UserApps/"+app_name+"/index.html")
				file.flush()
				file.close()
				#Execute using pyweview
				path = str(cl_path+"Apps/UserApps/"+app_name+"/index.html")
				if(platform.system() == "Windows"):
					path = path.replace("/", "\\")
				webview.create_window(name, path)
				print(path)
	def run_python_app(self, app_name):
		self.run(app_name)
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
		f.write("\n[app_type] => web")
		#Create the application, then import the requirements
		app_path = os.path.expanduser("~")+"/CApps/"+app_name
		app_path = app_path.replace("\\", "/")
		f = open(app_path+"/index.js", "w")
		sys.argv.remove("bot.py")
		if("--run-app" in sys.argv):
			sys.argv.remove("--run-app")
		f.write("function main(args){\n\tdocument.write(args);\n}\nmain("+str(sys.argv)+");")
		f.flush()
		f.close()
		#Write javascript file
		f = open(app_path+"/app.js", "w")
		f.write("function getName()\n{\n\treturn \""+app_name+"\";\n}")
		f.flush()
		f.close()
		#Write app file
		f = open(app_path+"/app.web", "w")
		f.write("[url] => file:///"+app_path+"/index.js")
		f.flush()
		f.close()

		#Write app.html
		f = open(app_path+"/index.html", "w")
		f.write("<html>\n\t<header>\n\t\t<script src=\"index.js\"></script>\n\t</header>\n</html>")
		f.flush()
		f.close()
		#Notify app was created
		print("Sample app stored in "+os.path.expanduser("~")+"/CApps/"+app_name)