import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import random
import pywhatkit
from keyboard import press
import subprocess as sp
import pywhatkit as pwt
import wikipedia as googleScrap
from pynput.keyboard import Key, Controller
import time
from pyautogui import click, leftClick, rightClick, doubleClick, tripleClick
keyboard=Controller()
import pyautogui
import winsound 
from winsound import PlaySound
# from playsound import playsound
import openai
import pyjokes
import bdi
import questions
# time.sleep(2)

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[1].id)

def speak(voice):
    engine.say(voice)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good morning,Sir!')
        print('Good morning,Sir!')
    elif hour>=12 and hour<16:
        speak('Good afternoon,Sir!')
        print('Good afternoon,Sir!')
    else:
        speak('Good evening,Sir!')
        print('Good evening,Sir!')
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        voice = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(voice, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
     
if __name__ == "__main__" :
    wishme()



print('Initialising your system.....')
speak('Initialising your system.....')
while True:
    a=(random.choice(questions.greetings) +  random.choice(questions.myself))
    print(a)
    speak(a)
    # print(random.choice(questions.greetings) +  random.choice(questions.myself))
    # speak(random.choice(questions.greetings) +  random.choice(questions.myself))
    # alpha = takeCommand().lower()
    alpha=input("Enter your message: ")
    b=(random.choice(questions.howyoufeel))
    print(b)
    speak(b)
    # print(random.choice(questions.howyoufeel))
    # speak(random.choice(questions.howyoufeel))
    howyoufeelans=input("Type here...")

    # my_list = ["apple", "banana", "cherry"]
    # sentence = "I love eating banana smoothies."

    for item in questions.sadfeeling:
        if item in howyoufeelans:
            beta=item
            print(beta)

    for itemh in questions.happyfeeling:
        if itemh in howyoufeelans:
            betah=itemh
            print(betah)