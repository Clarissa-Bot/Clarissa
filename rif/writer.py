from rif import reader
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("rif", "")
import sys
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
from rif import reader as rdr
from configparser import DuplicateSectionError
from configparser import NoSectionError
try:
	from configparser import SafeConfigParser
except ImportError:
	from ConfigParser import SafeConfigParser
s = SafeConfigParser(False)
import os
def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    #Remove original file
    #remove(file_path)
    #Move new file
    move(abs_path, file_path)
def setClarissaSettingWithPath(path, conf_sec, key, value):
	if(os.path.isfile(path)):
		f = open(path, 'a')
	else:
		f = open(path, 'w')
	repl = open(path, "r")
	result = ""
	for line in repl.readlines():
		if( "["+key+"] => " in line):
			replace(path, line, "")
	f.write("\n["+key+"] => "+value)
	f.flush()
	f.close()
def setClarissaSetting(conf_sec,key, value):
	if(reader.getClarissaSettingWithPath(dir_path+"settings.rif", "main","install") is not None):
		os.environ['CLARISSA_PATH'] = reader.getClarissaSettingWithPath(dir_path+"/settings.rif", "main", "install")
		setting_path = os.environ['CLARISSA_PATH']+"settings.rif"
		setClarissaSettingWithPath(setting_path, conf_sec, key, value)
	else:
		if(os.path.exists("Settings") is False):
			os.mkdir("Settings")
		setting_path = dir_path+"/settings.rif"
		setClarissaSettingWithPath(setting_path, conf_sec, key, value)
