import sqlite3

class SQL:
	def __init__(self, path):
		self.path = path

	def connect(self):
		self.db = sqlite3.connect(self.path)
		return self.db
	
	def use_commands(self, commands):
		self.connect()
		self.cursor = self.db.cursor()
		self.cursor.execute(commands)
		return self.cursor

	def finalize(self):
		self.db.commit()
		self.db.close()


	def get_results(self, table_name, to_select, selection_query=None):
		self.connect()
		if(selection_query == None):
			cursor = self.use_commands("SELECT "+to_select+" FROM "+table_name)
		else:
			cursor = self.use_commands("SELECT "+to_select+" FROM "+table_name+" WHERE "+selection_query)
		result = cursor.fetchall()
		return result
#Use this to write to a database
#Instead of constantly reading and printing