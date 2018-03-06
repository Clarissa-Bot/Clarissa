import random

respPart1 =open("corpus/learn_corpus.txt", 'r').readlines()
respPart2 =open("corpus/fun_corpus.txt", 'r').readlines()
respPart3 =open("corpus/ending_corpus.txt", 'r').readlines()

num =random.randrange(0, 4)

def learn(db_support):
    print("Learning data")

def learn_name(messageToBot):
    if(messageToBot.startswith("call me ")):
        return "Clarissa: Okay. I will call you "+messageToBot.replace("call me ", "")
    elif(messageToBot.startswith("Call me")):
        return "Clarissa: Okay. I will call you "+messageToBot.replace("Call me ", "")

def learn_hobby(inputText):
    if(inputText.startswith("I like to ")):
        print('Clarissa: '+(respPart1[num]+(respPart2[num]+(respPart3[num]))))
        return (respPart1[num]+(respPart2[num]+(respPart3[num])))
    elif(inputText.startswith("i like to ")):
        print('Clarissa: '+(respPart1[num]+(respPart2[num]+(respPart3[num]))))
        return (respPart1[num]+(respPart2[num]+(respPart3[num])))
