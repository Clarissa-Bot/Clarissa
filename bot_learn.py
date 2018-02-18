def learn(db_support):
    print("Learning data")

def learn_name(messageToBot):
    if(messageToBot.startswith("call me ")):
        return "Clarissa: Okay. I will call you "+messageToBot.replace("call me ", "")
    elif(messageToBot.startswith("Call me")):
        return "Clarissa: Okay. I will call you "+messageToBot.replace("Call me ", "")

def learn_hobby(inputText):
    if(hobbyText.startswith("I like to ")):
        print("Clarissa: That's a neat hobby!")
    elif(hobbyText.startswith("i like to ")):
        print("Clarissa: That's a neat hobby!")
    
