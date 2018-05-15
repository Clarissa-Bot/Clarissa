import sys, os

#Default Character class
class Character:

	def __init__(self, name):
		self.character_name = name
		self.character_level = 0
		self.character_age = 21
		self.times_shot = 0

	def increase_level(self, ammt_increased=1, name="Random"):
		self.character_level = self.character_level + ammt_increased
		print("\t"+name + " INCREASED TO "+str(self.character_level))

	def decrease_level(self, ammt_decreased=1, name="Random"):
		self.character_level = self.character_level - ammt_decreased
		print("\t"+name + " FELL TO "+str(self.character_level))
		if(self.get_level() <= 0):
			print(self.get_name()+" IS DEAD")
			exit()

	def get_level(self):
		return self.character_level

	def grow(self):
		self.character_age = character_age + 1