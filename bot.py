import os
import sys as sys
import bot_response as bot
import bot_learn as learner
import logger as log
import urllib
import writer as w
import reader as r
import reader
import urllib
from importlib import reload
from urllib.request import urlopen
import speech_recognition as speech_recognizer
import datetime
import time as time_check
import tts
import shutil
from libs.cpu import CPU
from libs.apps import Apps
from threading import Thread
from zipify.zipify import PAR
#Allow the user to communicate with the bot
#Also allow the bot to learn about the person
def getSpeech():
        #Initialize speech recognizer as reader
        reader = speech_recognizer.Recognizer()
        #Open speech recognizer
        with speech_recognizer.Microphone() as mic:
            #Listen for those sweet, sweet vocals
              audio = reader.listen(mic)
        try:
                #Remind them they are awesome
                print(r.getClarissaSetting("main","user.name")+": "+reader.recognize_google(audio))
                return reader.recognize_google(audio)
        except speech_recognizer.UnknownValueError:
                #Fuck, we fucked up
                if(r.getClarissaSetting("speech", "speak_out") == "true"):
                    tts.init("I'm sorry. I could not understand that.", 'en-US', False)
                print("Clarissa: I'm sorry. I could not understand that")
        except speech_recognizer.RequestError as error:
                #Fucking fuck cant keep fucking up shit fuck!
                if("recognition connection failed" in "{0}".format(error)):
                        if(r.getClarissaSetting("speech", "speak_out") == "true"):
                            tts.init("I need an internet connection for speech recognition. I will disable speech recognition. You can later re-enable it by running python bot.py --enable-speech-recognition", 'en-US', False)
                        print("Clarissa: I need an internet connection for speech recognition. I will disable speech recognition. You can later re-enable it by running python bot.py --enable-speech-recognition")
                        w.setClarissaSetting("speech", "hey_clarissa_enabled", "false")

                        toBot(messageToBot=input(r.getClarissaSetting("main","user.name")+": "))
                print("Clarissa: Could not process: {0}".format(error))
                if(r.getClarissaSetting("speech", "speak_out") == "true"):
                    tts.init("Could not process {0}".format(error), 'en-US', False)
        except (KeyboardInterrupt, SystemExit):
            #shutil.rmtree("Audio/", True)
            bot.getResponse("kill-bot")
#Check if voice recognition is enabled
#If so, alter clarissa_voice_recognition_enabled
clarissa_voice_recognition_enabled = False
if(r.getClarissaSetting("speech", "hey_clarissa_enabled") == "true"):
        clarissa_voice_recognition_enabled = True
#Replace def to replace pattern in file
def replace(file_path, pattern, subst):
        read = open(file_path, 'r')
        write = open(file_path, 'w')
        lines = read.read()
        print(read.read().replace(pattern, subst))
#Here is the gold!
def toBot(messageToBot):
    try:
            #Reload the bot and learner modules
            reload(bot)
            reload(learner)
            #If the message is none, go to getSpeech(), as that is
            #When we are needed
            if(messageToBot == None):
                    messageToBot = getSpeech()
            #Not relevant. Ignore, otherwise whole application combusts
            #Into an eternal pit of fire
            if(os.path.isfile(".bot_engage")):
                    print("You can only run one instance of Clarissa.")
            else:
                    #Not relevant, yet still works
                    swearNum = 1
                    #Remind the computer where CLARISSA_PATH is
                    os.environ['CLARISSA_PATH'] = r.getClarissaSettingWithPath("setup.rif", "main", "install")
                    #Just for shits and giggles, remind the computer who the user name is!
                    os.environ['USER_NAME'] = r.getClarissaSetting("main","user.name")
                    if(messageToBot == "--add-command"):
                            #Write command to server
                            writeCommand(command=input("Command: "), response=input("Responses: "))
                            reload(bot)
                    elif(messageToBot == "kill-bot"):
                            #Die, die, die!
                            exit()
                    elif(messageToBot == "--clear-commands"):
                            #Leave for multi-user computers. Clears the command list that is written.
                            os.remove("chat.log")
                            print("Cleared commands")
                            exit()
                    elif(messageToBot == "learn"):
                            #Ancient code, but will be used sometime soon.
                            learner.learn(db_support=False)
                    elif(messageToBot == "--get-commands"):
                            #Print out commands
                            commandsList = open("commands.list","r")
                            print(commandsList.read())
                    elif(messageToBot == "--get-logs"):
                            #Print out what has been said
                            logs = open('chat.log', 'r')
                            print(logs.read())
                    elif(messageToBot == "--update-clarissa"):
                            toBot("Hello!")
                    elif(messageToBot == "list the commands"):
                            toBot("Hello!")
                    elif("Call me " in messageToBot):
                            w.setClarissaSetting("main","user.name", messageToBot.replace("Call me ", ""))
                    elif("call me " in messageToBot):
                            w.setClarissaSetting("main","user.name", messageToBot.replace("call me ", ""))
                    elif("Run " in messageToBot):
                        #Runs an installed application
                        #Thank the lord I placed the code in another module
                        apps = Apps()
                        if(apps.does_app_exist(messageToBot.replace("Run ","")) == True):
                            apps.run(messageToBot.replace("Run ",""))
                            return None
                        else:
                            print(messageToBot.replace("Run ","")+" was not found")
                            if(clarissa_voice_recognition_enabled == True):
                                toBot(messageToBot=getSpeech())
                            else:
                                toBot(messageToBot=input(r.getClarissaSetting("main","user.name")+": "))
                    elif("run " in messageToBot):
                        #Same deal, but lower case
                        apps = Apps()
                        if(apps.does_app_exist(messageToBot.replace("run ","")) == True):
                            apps.run(messageToBot.replace("run ",""))
                            return None
                        else:
                            print(messageToBot.replace("run ","")+" was not found")
                            if(clarissa_voice_recognition_enabled == True):
                                toBot(messageToBot=getSpeech())
                            else:
                                toBot(messageToBot=input(r.getClarissaSetting("main","user.name")+": "))
                    elif("Make app" in messageToBot):
                        #Create an app
                        apps = Apps()
                        apps.make_app(input("App name:"))
                    elif("make app" in messageToBot):
                        #Same deal but in lower case
                        apps = Apps()
                        apps.make_app(input("App name:"))
                    #Log what was said for later review by user
                    log.log("chat.log", messageToBot)
                    #Initialize cpu hopper
                    cpu_def = CPU()
                    #Will only work on Windows, temporarily
                    cpu_def.run_code(code=bot.getResponse(messageToBot))
                    #Check if speech recognition is enabled
                    #If it is, messageToBot is None
                    if(clarissa_voice_recognition_enabled == True):
                            toBot(messageToBot=getSpeech())
                    else:
                            toBot(messageToBot=input(r.getClarissaSetting("main","user.name")+": "))
    except TypeError:
        #If there is an error, check if speech recognition is enabled
        if(clarissa_voice_recognition_enabled is True):
            #Use voice
            toBot(getSpeech())
        else:
            #Use normal
            toBot(messageToBot=input(r.getClarissaSetting("main","user.name")+": "))
    except (KeyboardInterrupt, SystemExit):
        #End on exit, 100% will fail first 5 seconds. Not my problem, user.
        bot.getResponse("kill-bot")
#Write a command to your own account
def writeCommand(command, response):
        commandList = open("commands.list", "w")
        commandList.write(command)
        commandList.flush()
        commandList.close()
        action = input("Action type (chat, reminder, play sound): ")
        if "Y" in input("Do you wish to upload the command to your account? ") or ("bremo" in os.environ['USERPROFILE'].short()):
                import requests as r
                url = 'http://softy.xyz/apps/sites/clarissa/update.php'
                query = {'u': reader.getClarissaSettingWithPath('user.rif', 'user', 'user'),
                'p': reader.getClarissaSettingWithPath('user.rif', 'pass', 'pass'),
                'c': command,
                        'r': response,
                        'a': action}
                res = r.post(url, data=query)
                print(res.text)
#Do a check if a string equals a string
#Don't judge, I was lazy.
def getIf(message, command, response):
	if(message == command):
		print("Clarissa: "+response)
	else:
		print("I do not understand "+message)

def updateCorpus():
    #Download corpus from server if asked to
    download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/chameleons.pdf", "Chameleons", "corpus/chameleons.pdf", delete=True)
    download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/movie_characters_metadata.txt", "Movie Characters Meta Data", "corpus/movie_characters_metadata.txt", delete=True)
    download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/movie_conversations.txt", "Movie Conversations", "corpus/movie_conversations.txt")
    download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/movie_lines.txt", "Movie Lines", "corpus/movie_lines.txt", delete=True)
    download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/movie_titles_metadata.txt", "Movie Titles", "corpus/movie_titles_metadata.txt", delete=True)
    download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/raw_script_urls.txt", "Raw Script", "corpus/raw_script_urls.txt", delete=True)
    download("https://softy.000webhostapp.com/apps/sites/clarissa/corpus/README.txt", "README", "corpus/README.txt", delete=True)
def download(url, title, path, delete=False):
    #Given the name, you do know what this is, right?
    if(os.path.exists(path) and delte is True):
        os.remove(path)
    print("Downloading: "+title)
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data
    f = open(path, "wb")
    f.write(text)
    f.flush()
    f.close()
swearNum = 0
time = datetime.datetime.now()
hour_min = (time.hour+time.minute)
if(hour_min is 1) and (r.getClarissaSetting("main", "auto_update") is "true"):
    #Update at 1 AM ONLY if auto update is on
    bt = Thread(target=updateCorpus)
    bt.start()
print("Welcome to Clarissa. If you need any help, run python bot.py --help")
#Check if auto update is enabled
if(r.getClarissaSetting("main","auto_update") is "true"):
        if(" 12:" or " 6:" in time):
                os.system("python update.py")
try:
        if("--add-command" in sys.argv):
                writeCommand(command=sys.argv[2], response=sys.argv[3])
                reload(bot)
        elif ("--clear-commands" in sys.argv):
                #os.remove("commands.bot")
                #os.remove("responses.bot")
                os.remove("bot_response.py")
                writeCommand("Hello", "Hi")
                reload(bot)
                print("Cleared commands")
        elif ("learn" in sys.argv):
                learner.learn(db_support=False)
        elif ("--get-commands" in sys.argv):
                commandsList = open("commands.list","r")
                print(commandsList.read())
        elif ("--update-clarissa" in sys.argv):
                os.system("python update.py")
                print("Clarissa: Updating won't work just yet.")
        elif ("--get-logs" in sys.argv):
                logs = open('chat.log','r')
                print(logs.read())
        elif ( sys.argv[1] == "set.name"):
                w.setClarissaSetting("main","user.name", sys.argv[2])
        elif ( sys.argv[1] == "--get-setting"):
                print(getClarissaSetting("main",sys.argv[2]))
        elif ( sys.argv[1] == "--update-from-url" ):
                os.system("python update.py --from-url "+sys.argv[2])
        elif ( "--enable-auto-update" in sys.argv):
                w.setClarissaSettingWithPath("Settings/Clarissa.rif","update","Clarissa.AUTO_UPDATE", "true")
        elif ("--update-bot" in sys.argv):
                os.system("python update.py")
        elif (sys.argv[1] == "--set-setting"):
                w.setClarissaSetting(sys.argv[2], sys.argv[3], sys.argv[4])
        elif ("--enable-speech-recognition" in sys.argv):
                w.setClarissaSetting("speech","hey_clarissa_enabled","true")
        elif ("--disable-speech-recognition" in sys.argv):
                w.setClarissaSetting("speech", "hey_clarissa_enabled", "false")
        elif ("--speak-out" in sys.argv):
                w.setClarissaSetting("speech", "speak_out", "true")
        elif ("--disable-speak-out" in sys.argv):
                w.setClarissaSetting("speech", "speak_out", "false")
        elif("--retrain" in sys.argv):
                print("This option existed in older versions. Now we use a dataset.")
        elif(sys.argv[1] == "--make-app"):
            app = Apps()
            app.make_app(sys.argv[2])
        elif(sys.argv[1] == "--text"):
            bot.getResponse(sys.argv[2])
        elif(sys.argv[1] == "--run-app"):
            messageToBot = sys.argv[2]
            apps = Apps()
            if(apps.does_app_exist(messageToBot.replace("Run ","")) == True):
                apps.run(messageToBot.replace("Run ",""))
            else:
                print(messageToBot.replace("Run ","")+" was not found")
                if(clarissa_voice_recognition_enabled == True):
                    toBot(messageToBot=getSpeech())
                else:
                    toBot(messageToBot=input(r.getClarissaSetting("main","user.name")+": "))
        elif(sys.argv[1] == "--install-app"):
            fp = os.path.expanduser("~")+"/CApps/"+sys.argv[2]+"/build/master.cpk"
            p = PAR(fp)
            p.depackage()
            print("Installed "+sys.argv[2])
            
        elif(sys.argv[1] == "--install-app" and "--from-external" in sys.argv):
            if(".cpk" in sys.argv[2]):
                fp = sys.argv[2]
                p = PAR(fp)
                p.depackage()
                print("Installed "+sys.argv[2])
            else:
                print("Failed to install app: Archive is not a valid Clarissa package.")
        elif(sys.argv[1] == "--build-app"):
            fp = os.path.expanduser("~")+"/CApps/"+sys.argv[2]
            p = PAR(fp)
            p.package(fp, sys.argv[3])
        elif(sys.argv[1] == "--build-app" and "--from-external" in sys.argv[4]):
            p = PAR(sys.argv[2])
            p.package(fp, sys.argv[3])
        elif("--help" in sys.argv or "--h" in sys.argv):
                print("Commands:")
                print("\t--add-command : Adds command to Clarissa")
                print("\t--clear-commands : Clears all added custom commands")
                print("\t--get-commands : Prints a list of Clarissa commands")
                print("\t--update-clarissa : Adds messages")
                print("\t--get-logs : Gets all the chat logs")
                print("\tset.name : Gives you a custom username")
                print("\t--get-setting: Gets settings stored")
                print("\t--set-setting: Sets clarissa setting (--set-setting [HEADER] [KEY] [VALUE]")
                print("\t--enable-auto-update : Turns on auto update feature for commands")
                print("\t--update-bot : Updates the list of existing commands (Will be used to update the bot later on)")
                print("\t--update-from-url: Get a custom messages update from your own site")
                print("\t--enable-speech-recognition: Allows you to control Clarissa with your voice")
                print("\t--disable-speech-recognition: Disables speech recognition")
                print("\t--speak-out: Allows Clarissa to talk (BETA, may be slow!)")
                print("\t--disable-speak-out: Stays to classic input output")
                print("\t--retrain: Retrains this bot")
                print("\t--make-app: Builds sample app to CApps directory (--make-app [APP_NAME])")
                print("\t--install-app: Installs application to Clarissa (--install-app [CPK_PATH])")
                print("\t--run-app: Runs app (python bot.py --run-app [APP_NAME])")
                print("\t--build-app: Builds application to .cpk (--build-app APP_PATH CPK_NAME)")
                print("\t--h / --help : Prints this list")
        else:
                if(clarissa_voice_recognition_enabled is True):
                        toBot(getSpeech())
                else:
                        toBot(messageToBot=input(r.getClarissaSetting("main","user.name")+": "))

except IndexError:
        if(clarissa_voice_recognition_enabled is True):
                print("Clarissa: Speak now")
                toBot(getSpeech())
        else:
                toBot(messageToBot=input(r.getClarissaSetting("main","user.name")+": "))