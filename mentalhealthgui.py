import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import random
import pywhatkit
import subprocess as sp
from pynput.keyboard import Key, Controller
import time
import pyautogui
import winsound
import openai
import pyjokes
import bdi
import runpy
import questions

import tkinter as tk
from tkinter import messagebox, scrolledtext

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
keyboard = Controller()

def speak(voice):
    engine.say(voice)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        return 'Good morning, Sir!'
    elif hour >= 12 and hour < 16:
        return 'Good afternoon, Sir!'
    else:
        return 'Good evening, Sir!'

def respond_to_feeling(user_input):
    beta = None
    for item in questions.feeling:
        if item in user_input:
            beta = item
            break
    if beta in questions.sadfeeling:
        response = f"Why are you feeling {beta}?\nDon't worry!\n" + random.choice(questions.myself) + random.choice(questions.santawna)
        return response, 'sad'
    elif beta in questions.happyfeeling:
        response = f"Ohh woww!\nWhy are you feeling {beta}?\n" + random.choice(questions.myself) + random.choice(questions.happy)
        return response, 'happy'
    else:
        return "Sorry, I couldn't understand your feeling.", 'unknown'

def start_session():
    greeting = random.choice(questions.greetings) + random.choice(questions.myself)
    return greeting

def process_problem(probans):
    probans = probans.lower().replace(" ", "_")
    problem_categories = {
        "personal_struggles": questions.personal_struggles,
        "career_and_financial_pressures": questions.career_and_financial_pressures,
        "relationships_and_social_pressures": questions.relationships_and_social_pressures,
        "existential_and_psychological_factors": questions.existential_and_psychological_factors,
        "external_factors": questions.external_factors,
        "emotional_reasons_for_feeling_alone": questions.emotional_reasons_for_feeling_alone,
        "physical_and_mental_exhaustion": questions.physical_and_mental_exhaustion,
        "suicidal_thoughts": questions.suicidal_thoughts
    }
    if probans in problem_categories:
        return random.choice(problem_categories[probans])
    else:
        return "Sorry, I don't recognize that problem category."

# GUI Code
class MentalHealthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mental Health Support")
        self.root.geometry("600x600")

        self.chat_window = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state='disabled')
        self.chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=10, pady=5, fill=tk.X)
        self.entry.bind('<Return>', self.send_message)

        self.start_session_gui()

    def speak_and_display(self, text):
        self.chat_window['state'] = 'normal'
        self.chat_window.insert(tk.END, f"Bot: {text}\n")
        self.chat_window['state'] = 'disabled'
        self.chat_window.see(tk.END)
        speak(text)

    def send_message(self, event=None):
        user_input = self.entry.get()
        self.chat_window['state'] = 'normal'
        self.chat_window.insert(tk.END, f"You: {user_input}\n")
        self.chat_window['state'] = 'disabled'
        self.entry.delete(0, tk.END)

        response, status = respond_to_feeling(user_input)
        self.speak_and_display(response)

        if status == 'sad':
            followup = "Would you like to talk with me, take the BDI test, or end this session?"
            self.speak_and_display(followup)

        elif status == 'happy':
            self.speak_and_display("I'm glad to hear that! 😊")

    def start_session_gui(self):
        greeting = wishme()
        self.speak_and_display(greeting)
        intro = start_session()
        self.speak_and_display(intro)

if __name__ == "__main__":
    root = tk.Tk()
    app = MentalHealthApp(root)
    root.mainloop()
