print("Updating Clarissa")
import urllib.request, urllib.error, urllib.parse
import json
import os as os
import sys as sys
import logger as log
from urllib.request import urlopen

url = ""
try:
	if ( sys.argv[1] == "--from-url"):
		url = sys.argv[2]
	else:
		url = "http://softy.xyz/apps/sites/clarissa/get.php"
		urllib.request.urlretrieve("http://softy.xyz/apps/sites/clarissa/clarissa.json", "list.json")
except IndexError:
		url = "http://softy.xyz/apps/sites/clarissa/get.php"
		urllib.request.urlretrieve("http://softy.xyz/apps/sites/clarissa/clarissa.json", "list.json")
if(os.path.isfile("list.json")):
	os.system("rm -R list.json")
req = urllib.request.Request(url)
opener = urllib.request.build_opener()
f = opener.open(req)
json = json.loads(f.read())

for line in range(len(json)):
	file = open("list.json",'a')
	file.write(str(json))
	commandList = open("commands.list", "a")
	commandList.write(json[line]['command']+"\n")
	commandList.flush()
	commandList.close()
	file.flush()
	file.close()
	

def getServerBasedResponse(to_bot):
	url = "http://softy.xyz/apps/sites/clarissa/get.php"
	req = urllib.request.Request(url)
	opener = urllib.request.build_opener()
	file = opener.open(req)
	json = json.loads(f.read())
	while line in range(len(json)):
		if(to_bot is json[line]['command']):
			return json[line]['reply']
print("Update was successful")