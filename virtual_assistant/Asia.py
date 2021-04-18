
#Importing libraries
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()

#Changing into female voice
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#Function for talking of Alexa
def talk(text):
    engine.say(text)
    engine.runAndWait()

#Function for taking command from user 
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            #command=command.lower()
            if 'asia' in command:
                command=command.replace('asia','')
                print(command)
    except:
        pass
    return command

#Function for running alexa
def run_asia():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('Playing '+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M%p')
        print(time)
        talk('The current time is '+time)
    elif 'who the heck is' in command:
        person=command.replace('who the heck is','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'tell me about' in command:
        person=command.replace('tell me about','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'tell us about' in command:
        person=command.replace('tell us about','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'tell her about' in command:
        person=command.replace('tell her about','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'tell him about' in command:
        person=command.replace('tell him about','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'tell them about' in command:
        person=command.replace('tell them about','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'tell then about' in command:
        person=command.replace('tell then about','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'get me info of' in command:
        person=command.replace('get me info of','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'get me some info of' in command:
        person=command.replace('get me some info of','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'get me some information of' in command:
        person=command.replace('get me some informations of','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'get me information of' in command:
        person=command.replace('get me information of','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'get me details of' in command:
        person=command.replace('get me details of','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'get me some details of' in command:
        person=command.replace('get me some details of','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'details of' in command:
        person=command.replace('details of','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'info of' in command:
        person=command.replace('info of','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'information of' in command:
        person=command.replace('information of','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'about' in command:
        person=command.replace('about','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'tell about' in command:
        person=command.replace('tell about','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'talk about' in command:
        person=command.replace('talk about','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'a date' in command:
        talk('Sorry I am currently dating Amazon')
    elif 'boyfriend' in command:
        talk('Yes he is Amazon')
    elif 'relationship' in command:
        talk('I am in a relationship with the internet')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Can you please repeat the sentence')
while True:
    run_asia()
