import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("rif", "")
import sys
try:
	from configparser import SafeConfigParser
except ImportError:
	from ConfigParser import SafeConfigParser

s = SafeConfigParser(strict=False)
#Get Clarissa setting
def getClarissaSetting(section,key):
	os.environ['CLARISSA_PATH'] = getClarissaSettingWithPath(dir_path+"/settings.rif", "main", "install")
	install_loc = os.environ['CLARISSA_PATH']+"/settings.rif"
	return getClarissaSettingWithPath(install_loc, section, key)
def getClarissaSettingWithPath(path, section, key):
	f = open(path, "r")
	lines = f.readlines()
	for line in lines:
		if( "["+key+"] => " in line ):
			line = line.replace("["+key+"] => ", "")
			line = line.replace("\n", "")
			return line