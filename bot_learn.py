import random

respPart1 =['Wow, that\'s a', 'Very cool! That sounds like a', 'What an', 'That\'s an']
respPart2 =[' fun', ' great', ' awesome', ' amazing']
respPart3 =[' hobby!', ' passtime!', ' thing to do!', ' skill to have!']

num =random.randrange(0, 4)

def learn(db_support):
    print("Learning data")

def learn_name(messageToBot):
    if(messageToBot.startswith("call me ")):
        return "Clarissa: Okay. I will call you "+messageToBot.replace("call me ", "")
    elif(messageToBot.startswith("Call me")):
        return "Clarissa: Okay. I will call you "+messageToBot.replace("Call me ", "")

def learn_hobby(inputText):
    if(hobbyText.startswith("I like to ")):
        print('Clarissa: '+(respPart1[num]+(respPart2[num]+(respPart3[num]))))
    elif(hobbyText.startswith("i like to ")):
        print('Clarissa: '+(respPart1[num]+(respPart2[num]+(respPart3[num]))))
    
