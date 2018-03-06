import os
import random

#Massive learning ability
def mass_learn():
	print("Mass learning!")
	text_list = ["Hello", "How", "Are", "I", "Am", "You"]
	string = ""
	for i in range(0, 4):
		r = random.randrange(0, len(text_list) - 1)
		string += text_list[r] + " "
	print(string)
mass_learn()