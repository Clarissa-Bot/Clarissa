import os
import sys
try:
	from configparser import SafeConfigParser
except ImportError:
	from ConfigParser import SafeConfigParser

s = SafeConfigParser(strict=False)
#Get Clarissa setting
def getClarissaSetting(section,key):
	os.environ['CLARISSA_PATH'] = getClarissaSettingWithPath("setup.ini", "main", "install")
	install_loc = os.environ['CLARISSA_PATH']+"/Settings/Clarissa.ini"
	s.read(install_loc)
	return s.get(section, key)
def getClarissaSettingWithPath(path, section, key):
	s.read(path)
	return s.get(section, key)