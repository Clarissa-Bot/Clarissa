from characters import Character
import sys, os

#Default class for Shooter and response team
class Shooter(Character):

	def injure(self, ammt=1):
		if(self.get_level() <= 0):
			self.shooter_age = 0
			print("SHOOTER "+self.get_name()+" IS DEAD")
			self.die()
			exit()
		else:
			print("SHOOTER "+self.get_name()+" WAS BADLY INJURED")
			self.times_shot += 1
		self.decrease_level(name=self.get_name())
	def die(self):
		pass

	def get_age(self):
		return self.character_age

	def set_position(self, x, y):
		self.x_pos = x
		self.y_pos = y
		os.system("cls")

	def get_x(self):
		return self.x_pos

	def get_y(self):
		return self.y_pos

	def get_name(self):
		return self.character_name

	def shoot_at(self, x, y, characters, rpm=1):
		rpm = rpm * self.get_level()
		for character in characters:
			if(character.get_x() == x):
				if(character.get_y() == y):
					self.target = character
					print(self.get_name() + " FIRED SHOTS AT "+self.target.get_name())
					print("\tRPM: "+str(rpm))
					self.target.injure(rpm)
					self.increase_level(name=self.get_name())
					return "FIRED!"
			elif(self.get_x() == x):
				if(self.get_y() == y):
					self.target = character
					print(self.get_name() + " INJURED THEMSELF")
					self.injure(rpm)
					self.decrease_level(name=self.get_name())
					return "FIRED!"
		print(self.get_name() + " ATTEMPTED TO FIRE SHOTS BUT FAILED")
		self.decrease_level(name=self.get_name())