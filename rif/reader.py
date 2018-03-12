import os
import sys
try:
	from configparser import SafeConfigParser
except ImportError:
	from ConfigParser import SafeConfigParser

s = SafeConfigParser(strict=False)
#Get Clarissa setting
def getClarissaSetting(section,key):
	os.environ['CLARISSA_PATH'] = getClarissaSettingWithPath("setup.rif", "main", "install")
	install_loc = os.environ['CLARISSA_PATH']+"/Settings/Clarissa.rif"
	return getClarissaSettingWithPath(install_loc, section, key)
def getClarissaSettingWithPath(path, section, key):
	f = open(path, "r")
	lines = f.readlines()
	for line in lines:
		if( "["+key+"] => " in line ):
			line = line.replace("["+key+"] => ", "")
			line = line.replace("\n", "")
			return line