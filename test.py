from time import sleep
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

message = 'hello'
for i in range(len(message), 0, -1):
    cls()
    print (message[:i])
    sleep(1)