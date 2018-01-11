import sys as sys
def out(line):
	print(line)

def log(file, line):
	file = open(file, 'w')
	file.write("[LOG]"+line)
	file.flush()
	file.close()

def log_sample(line):
	log('file.log', line)

if(sys.argv[1] == "--log-out"):
	log(sys.argv[2], sys.argv[3])