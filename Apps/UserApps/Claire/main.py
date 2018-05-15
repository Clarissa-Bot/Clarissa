from app import App
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
app = App(dir_path)
def main(args):
	app.set_name("Claire")
app.on_exit()