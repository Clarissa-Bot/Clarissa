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
		os.system("git reset --hard HEAD")
		os.system("git fetch")