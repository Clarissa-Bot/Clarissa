from termcolor import colored, cprint
import sys
import os
import libs.cp as cp
import multiprocessing as mp
import random
class CPU:
	def __init__(self, cpu_num=0):
		if(cpu_num is 0):
			cpu_num=random.randint(1, mp.cpu_count())*1
		self.init_from_cpu(cpu_num)
	def init_from_cpu(self, cpu_num):
		self.blacklisted = set()
		if(os.path.exists("blacklisted_cpu.list")):
			f = open("blacklisted_cpu.list","r")
			for line in f.readline():
				self.blacklisted.add(str(line))
		#Check if this cpu is blacklisted
		if(str(cpu_num) in self.blacklisted):
			print("CPU cannot be used")
			return None
		self.cpu = cpu_num

	def run_code(self, code):
		if("--print-log" in sys.argv):
			print("Switching to CPU number "+str(self.cpu))
		cp.set_process_affinity_mask(os.getpid(), self.cpu)
		exec(code)

	def blacklist_cpu(self):
		#Blacklist cpu
		if(os.path.exists("blacklisted_cpu.list")):
			f = open("blacklisted_cpu.list", "a")
		else:
			f = open("blacklisted_cpu.list", "w")
		f.write(str(self.cpu)+"\n")
		f.flush()
		f.close()
		self.blacklisted.add(str(self.cpu))
		print("Blacklisted "+str(self.cpu))

	def reenlist_cpu(self):
		if(str(self.cpu) in self.blacklisted):
			self.blacklisted.remove(str(self.cpu))
		f = open("blacklisted_cpu.list", "r")
		cpu_num = ""
		for line in f.readline():
			cpu_num += line

		cpu_num = cpu_num.replace(str(self.cpu), "")
		f = open("blacklisted_cpu.list", "w")
		f.write(cpu_num)
		f.flush()
		f.close()
		print("Re-enlisted CPU")