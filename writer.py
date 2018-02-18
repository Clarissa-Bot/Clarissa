import reader
import os
import sys
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import reader as rdr
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
	try:
		content = open(path, "r").readlines()
		s.add_section(conf_sec)
	except DuplicateSectionError:
		pass
	except NoSectionError:
		s.add_section(conf_sec)
	s.set(conf_sec, key, value)
	s.write(f)
	f.flush()
	f.close()
def setClarissaSetting(conf_sec,key, value):
	os.environ['CLARISSA_PATH'] = reader.getClarissaSettingWithPath("setup.ini", "main", "install")
	setting_path = os.environ['CLARISSA_PATH']+"/Settings/Clarissa.ini"
	setClarissaSettingWithPath(setting_path, conf_sec, key, value)
