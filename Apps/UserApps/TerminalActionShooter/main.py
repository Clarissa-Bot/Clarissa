from app import App
import os
from shooter import Shooter
from officer import Officer
import sys, os
dir_path = os.path.dirname(os.path.realpath(__file__))

print("Welcome to Action Shooter, the terminal based python game!")
print("The only rules are to not share your position and to have fun!")
print("Fact: The more you injure your enemy, the stronger you get,and the weaker they get.")
print("The more the enemy injures you, the weaker you get, and the stronger they get.")
print("The game ends when one of the players' strength is at ZERO.")
print("You also get weaker if you miss the shot you make!")
app = App(dir_path)
shooter1 = Shooter(input("Player 1, your name: "))
shooter_x = int(input("Your X position: "))
shooter_y = int(input("Your Y position: "))
os.system("cls")

officer1 = Officer(input("Player 2, your name: "))
officer_x = int(input("Your X position: "))
officer_y = int(input("Your Y position: "))
shooter1.set_position(shooter_x, shooter_y)
officer1.set_position(officer_x, officer_y)

shooter1.increase_level(name=shooter1.get_name(), ammt_increased = 5)
officer1.increase_level(name=officer1.get_name(), ammt_increased = 5)

characters = [officer1, shooter1]

def main(args):
	play()


def play():
	shooter1.shoot_at(int(input("P1 X: ")), int(input("P1 Y: ")), characters)
	officer1.shoot_at(int(input("P2 X: ")), int(input("P2 Y: ")), characters)
	play()

app.on_exit()

