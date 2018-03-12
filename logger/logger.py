import sys as sys

def get_logs(file):
	log = open(file, 'r')
	print(log.read())

def log(file, message):
	log  = open(file, 'a')
	log.write("[LOG]"+message+"\n")
	log.flush()
	log.close()


def write_sample():
	log("sample.log", "This is a sample log file.")

#This code must be run from python on terminal
#Or python class

#We are using this in Clarissa