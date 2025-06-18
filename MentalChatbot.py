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
import runpy
import questions
# time.sleep(2)

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[0].id)

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

    for item in questions.feeling:
        if item in howyoufeelans:
            beta=item

    # for itemh in questions.happyfeeling:
    #     if itemh in howyoufeelans:
    #         betah=itemh

    # if 'sad' in howyoufeelans or 'low' in howyoufeelans or 'guilty' in howyoufeelans or 'failure' in howyoufeelans or 'worthless' in howyoufeelans and 'tired' in howyoufeelans and 'alone' in howyoufeelans and 'cry' in howyoufeelans:
    if beta in howyoufeelans and beta in questions.sadfeeling:
      
      print('Why are you feeling '+ beta)
      speak('Why are you feeling '+ beta)


      ans=input("Type here...")
      print("Don't worry!")
      speak("Don't worry!")
      c=(random.choice(questions.myself)) + random.choice(questions.santawna)
      print(c + '😉')
      speak(c)



      print("Would you like to talk with me? or will you give the BDI test? or end this session?")
      speak("Would you like to talk with me? or will you give the BDI test? or end this session?")


      talkortest=(input("Type here..."))

      if 'no' in talkortest or 'end' in talkortest:
          print("Terminating session...")
          exit()


      if 'bdi' in talkortest:
          runpy.run_path("bdi.py")

      if 'talk' in talkortest or 'yes' in talkortest:
          print("Okay, From what kind of problem are you going through?")
          speak("Okay, From what kind of problem are you going through?")

        #   my_list = ["apple", "banana", "cherry"]

          for item in questions.problems:
              print("Are you going through " + item)
              speak("Are you going through " + item)

 
          probans=input("Type here...")


        #   my_list = ["apple", "banana", "cherry"]

          try:
              index = questions.problems.index(probans)
              print(f"Element found at index {index}")
          except ValueError:
              print("Element not found")

          print(probans)

          probans=probans.lower()
          probans=probans.replace(" ","_")
          print(probans)

          if probans=="personal_struggles" :
              for item in questions.personal_struggles:
                  ps=random.choice(questions.personal_struggles)
                  print(ps)
                  speak(ps)

                  psans=input("Type here...")\
                  
          if probans=="career_and_financial_pressures" :
              for item in questions.career_and_financial_pressures:
                  ps=random.choice(questions.career_and_financial_pressures)
                  print(ps)
                  speak(ps)

                  psans=input("Type here...")

          if probans=="relationships_and_social_pressures" :
              for item in questions.relationships_and_social_pressures:
                  ps=random.choice(questions.relationships_and_social_pressures)
                  print(ps)
                  speak(ps)

                  psans=input("Type here...")

          if probans=="existential_and_psychological_factors" :
              for item in questions.existential_and_psychological_factors:
                  ps=random.choice(questions.existential_and_psychological_factors)
                  print(ps)
                  speak(ps)

                  psans=input("Type here...")


          if probans=="external_factors" :
              for item in questions.external_factors:
                  ps=random.choice(questions.external_factors)
                  print(ps)
                  speak(ps)

                  psans=input("Type here...")


          if probans=="emotional_reasons_for_feeling_alone" :
              for item in questions.emotional_reasons_for_feeling_alone:
                  ps=random.choice(questions.emotional_reasons_for_feeling_alone)
                  print(ps)
                  speak(ps)

                  psans=input("Type here...")

          if probans=="physical_and_mental_exhaustion" :
              for item in questions.physical_and_mental_exhaustion:
                  ps=random.choice(questions.physical_and_mental_exhaustion)
                  print(ps)
                  speak(ps)

                  psans=input("Type here...")

          if probans=="suicidal_thoughts" :
              for item in questions.suicidal_thoughts:
                  ps=random.choice(questions.suicidal_thoughts)
                  print(ps)
                  speak(ps)

                  psans=input("Type here...")

          print("Okay, i can understand. I am always with you.😊")
          speak("Okay, i can understand. I am always with you.")


    if beta in howyoufeelans and beta in questions.happyfeeling:
      print("Ohh woww!")
      speak("Ohh woww!")
      hpp=random.choice(questions.happyfeeling)
      print('Ohh well, Why are you feeling '+ beta)
      speak('Ohh well, Why are you feeling '+ beta)


      ans=input("Type here...")
      print("Ohh, that's great!")
      speak("Ohh, that's great!")
      c=(random.choice(questions.myself)) + random.choice(questions.happy)
      print(c + '😉')
      speak(c)

        #   print("Ohh woww!")
        #   speak("Ohh woww!")
        #   d=(random.choice(questions.myself)) + random.choice(questions.happyreaction)
        #   print(d)
        #   speak(d)

        #   if probans=="happy" :
        #       for item in questions.happy:
        #           ps=random.choice(questions.happy)
        #           print(ps)
        #           speak(ps)

        #           psans=input("Type here...")


        #   print("Okay, i can understand. I am always with you.😊")
        #   speak("Okay, i can understand. I am always with you.😊")

      