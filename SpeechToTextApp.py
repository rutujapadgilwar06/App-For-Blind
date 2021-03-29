import speech_recognition as sr 
import playsound
from gtts import gTTS 
import os
import random as ran
from word2number import w2n


def goodByeFunc(notInOurHands = False):
    if notInOurHands == True:
        assistant_speaks("I think we can not help you in this.")    
    assistant_speaks("Thank you for using uber. Please give us chance to help you again")
    return True


num = 1
def assistant_speaks(output):
    global num
    # num to rename every audio file 
    # with different name to remove ambiguity
    num += 1
    print("PerSon : ", output)
    toSpeak = gTTS(text = output, lang ='en', slow = False)
    # saving the audio file given by google text to speech
    file = str(num)+".mp3" 
    toSpeak.save(file)
    # playsound package is used to play the same file.
    playsound.playsound(file, True) 
    os.remove(file)
  
def get_audio(recheck = False):
    rObject = sr.Recognizer()
    audio = ''
    audioIsOkay = 1
    for i in range(3):
        with sr.Microphone() as source:
            print("Speak...")
            # recording the audio using speech recognition
            audio = rObject.listen(source, phrase_time_limit = 5) 
        print("Stop.") # limit 5 secs
        try:
            text = rObject.recognize_google(audio, language ='en-US')
            print("You : ", text)
            if recheck:
                assistant_speaks("You said : " + text + ". Is it correct? Please say yes or no.")
                humanVoice = get_audio().lower()
                if "yes" in humanVoice :
                    return text
                elif "no" in humanVoice:
                    assistant_speaks("Please say again")
                else:
                    goodByeFunc(True)
            else:
                return text
        except:
            assistant_speaks("Could not understand your audio, Please try again!")
            if i == 2:                
                audioIsOkay = 0
    if audioIsOkay == 0:
        assistant_speaks("Sorry we did not speak your language")
        goodByeFunc(True)
        raise Exception("dirty command")
    return true
        

def uberApp():
    assistant_speaks("What can we do for you?")
    assistant_speaks("Do you want cab or food? Please say from cab or food. You can also say no")
    stringOfUser = get_audio().lower()
    if "cab" in stringOfUser:
        cab()
    elif "food" in stringOfUser:
        food()
    else:
        goodByeFunc(True)

def foodDelivery(food):
    assistant_speaks("How much money do you want to spend on " + food + " in rupee")
    stringOfUser = get_audio().lower()
    stringOfUser = int(w2n.word_to_num(stringOfUser))
    assistant_speaks("We find best deal for you. Your order cost " + str(stringOfUser) + " from restaurant paradise with rating for food is four point two. Do u want to order? Please say yes or no.")
    stringOfUser = get_audio().lower()
    if "yes" in stringOfUser:
        assistant_speaks("Your order is placed, We will notify you when your order is 50 meter apart") 
        goodByeFunc()
    elif "no" in stringOfUser:
        goodByeFunc()
    else:
        goodByeFunc(True)

def food():
    assistant_speaks("What do you want to order?")
    assistant_speaks("We have Biryani, Pavbhaji and Pizza")
    foodofUser = get_audio().lower()
    if "biryani" in foodofUser.lower():
        foodDelivery("biryani")
    elif "pavbhaji" in foodofUser.lower():
        foodDelivery("pavbhaji")
    elif "pizza" in foodofUser.lower():
        foodDelivery("pizza")

def cabBooked(fair):
    assistant_speaks(fair + " rupee fair for your booking. We will notify you when cab is at 100 meter apart. Drive name is Will smith.")
    goodByeFunc()

def cab():
    assistant_speaks("We will access your current location for pick up point.")
    assistant_speaks("Where should i drop you.")
    stringOfUser = get_audio().lower()
    assistant_speaks(stringOfUser + " is your drop point. Is it correct? Please say yes or no")
    stringOfUser = get_audio().lower()
    if "yes" in stringOfUser:
        km = str(ran.randint(0,15))
        me = str(ran.randint(0,10))
        assistant_speaks("Distance of your ride is " + km + " kilometer and " + me + "meter")
        assistant_speaks("We have three rides for you. Uber X cost you " + str((int(km) * 15) + int(me)) + ". Uber pool cost you " + str((int(km) * 10) + int(me)) + ". Uber comfort cost you " + str((int(km) * 20) + int(me)) + ". Please say from x or pool or comfort for cab.")
        stringOfUser = get_audio().lower()
        if "x" in stringOfUser:
            cabBooked(str((int(km) * 10) + int(me)))
        elif "pool" in stringOfUser:
            cabBooked(str((int(km) * 15) + int(me)))
        elif "comfort" in stringOfUser:
            cabBooked(str((int(km) * 20) + int(me)))
        else:
            goodByeFunc(True)    
    elif "no" in stringOfUser:
        print("terminted")
        goodByeFunc()
    else:
        goodByeFunc(True)


if __name__ == "__main__":
    assistant_speaks("Hi, Good to hear you, What's your name, ?")
    name ='Human'
    name = get_audio()
    assistant_speaks("Hello, " + name + '.')
    assistant_speaks("Please say hi uber to open Uber")
    while(1):
        text = get_audio().lower()
        if "uber" in text:
            uberApp()
        elif "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            goodByeFunc()
            break
