import datetime
import bot_response
class App:
	def __init__(self, path):
		self.path = path

	def get_name(self):
		#Return name of application
		return self.get_result("name")
	def get_update_url(self):
		#Get the application's update url
		return self.get_result("update_url")
	def state_to_clarissa(self,text):
		#Ask Clarissa something
		bot_response.getResponse(text)
	def get_result(self, key):
		#Get key results
		f = open(self.path+"/info.rif", "r")
		text = f.readlines()
		result = ["Null"]
		for line in text:
			if("["+key+"] => "in line):
				if(result[0] == "Null"):
					del result[0]
				line = line.replace("["+key+"] => ", "")
				result.append(line)
		return result
	def update(self,path):
		#Update the whole project
		title = self.get_name()
		url = self.get_update_url()
		print("Downloading: "+title)
		response = urllib.request.urlopen(url)
		data = response.read()
		text = data
		f = open(path, "wb")
		f.write(text)
		f.flush()
		f.close()
	def log(self, text):
		#Log text
		print(datetime.datetime.now + ":"+text)
	def read(self, path):
		return open(path, "r").readlines()
	def write(self, path):
		return open(path, "w")