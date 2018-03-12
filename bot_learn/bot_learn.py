import random

line1 = open("corpus/learn_corpus.txt", 'r').readlines()
line2 = open("corpus/fun_corpus.txt", 'r').readlines()
line3 = open("corpus/ending_corpus.txt", 'r').readlines()

respPart1 = []
respPart2 = []
respPart3 = []



#Strip the strings of any new lines on all files.
for line_learn in line1:
    line_learn.replace("\n", "")
    respPart1.append(line_learn.rstrip())

for line_fun in line2:
    line_fun.replace("\n", "")
    respPart2.append(line_fun.rstrip())

for line_ending in line3:
    line_ending.replace("\n", "")
    respPart3.append(line_ending.rstrip())

num =random.randrange(0, len(respPart1) -1) #Get the length and deduct 1 for safety
num0 =random.randrange(0, 7)
num1 =random.randrange(0, 4)

def learn(db_support):
    print("Learning data")

def learn_name(messageToBot):
    if(messageToBot.startswith("call me ")):
        return "Clarissa: Okay. I will call you "+messageToBot.replace("call me ", "")
    elif(messageToBot.startswith("Call me")):
        return "Clarissa: Okay. I will call you "+messageToBot.replace("Call me ", "")

def learn_hobby(inputText):
    if(inputText.startswith("I like to ")):
        print('Clarissa: '+(respPart1[num]+(respPart2[num0]+(respPart3[num1]))))
        return (respPart1[num]+(respPart2[num0]+(respPart3[num1])))
    elif(inputText.startswith("i like to ")):
        print('Clarissa: '+(respPart1[num]+(respPart2[num0]+(respPart3[num1]))))
        return (respPart1[num]+(respPart2[num0]+(respPart3[num1])))
