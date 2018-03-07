import os, sys
import zipfile
from os import listdir
from os.path import isfile, join
import writer
import reader
import shutil

class PAR:
	def __init__(self, path):
		self.PATH = path
	def look_for(self, path, to_look_for):
		r = reader.getClarissaSetting(path, "main",to_look_for)
		return r

	def package(self, my_dir,par_name):
		if(os.path.exists(my_dir+"/build") is False):
			os.mkdir(my_dir+"/build")
		zipf = zipfile.ZipFile(my_dir+"/build/"+par_name+".cpk", 'w', zipfile.ZIP_DEFLATED)
		files = [f for f in os.listdir(my_dir) if("build" not in f)]
		for file in files:
			zipf.write(my_dir+"/"+file, file)
		print("Done!")

	def depackage(self):
		if(os.path.exists("Apps") is False):
			os.mkdir("Apps")
		with zipfile.ZipFile(self.PATH, 'r') as name_zip:
			with name_zip.open("info.rif") as name_info:
				print("Installing "+self.get_cpk_name())
				app_name = self.get_cpk_name()
				name_zip.extractall("Apps/"+str(app_name))



	def get_cpk_name(self):
		return self.get_from_cpk("main", "name")
	def get_from_cpk(self, section, key):
		with zipfile.ZipFile(self.PATH, 'r') as name_zip:
			with name_zip.open("info.rif") as name_info:
				name_zip.extract("info.rif")
				st = str(reader.getClarissaSettingWithPath("info.rif", section, key))
				os.remove("info.rif")
				return st