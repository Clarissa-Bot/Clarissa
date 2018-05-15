from app import App
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
app = App(dir_path)
def main(args):
	os.remove("main.py")
	print("Deleted")
app.on_exit()