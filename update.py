import sys, os, shutil
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("bot", "")
from rif import writer as w
from rif import reader as r

class Updater:
	def __init__(self, path):
		#Set the update path
		w.setClarissaSetting("update", "update_dir", path)
		self.path = r.setClarissaSetting("update", "update_dir")
	def update():
		main = r.getClarissaSetting("update", "update_dir")
		for root, sub, files in os.walk(main):
			for folder in sub:
				if(".git" in folder):
					return None
				outputFile = main + "/" + folder +"/crybaby.py"
				for file in files:
					filePath = main + "/" + file
					os.remove(filePath)
				os.rmdir(folder)
		os.system("git clone https://github.com/Clarissa-Bot/Clarissa.git -b test "+main)
folder = dir_path
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)