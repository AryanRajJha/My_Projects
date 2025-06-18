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

import time
from pyautogui import click, leftClick, rightClick, doubleClick, tripleClick
# keyboard=Controller()
import pyautogui
import winsound 
from winsound import PlaySound
# from playsound import playsound
import openai


greetings=["Hello ","Hii ","Hey ","Wassup "]
myself=["Sir ", "Boss ", "Dear ", "My dear ", "My friend ", "friend "]
# rand_greet=random.",c"hoice(greetings)
# print(rand_greet)

howyoufeel=["How are you?",
"How's it going?",
"How have you been?",
"How are things?",
"How's life?",
"What's up?",
"How's your day going?",
"How do you feel today?",
"How's everything?",
"How's your mood?",
"How are you holding up?",
"How do you feel?",
"How's your mood?",
"How are you doing emotionally?",
"How are you holding up?",
"How's your state of mind?",
"How's your heart today?",
"Are you feeling okay?",
"How's your energy level?",
"What's your vibe today?",
"How have you been feeling lately?",
"How do you feel today?",
"How's your mood today?",
"How are you doing today?",
"How's your day going emotionally?",
"Are you feeling okay today?",
"What's your vibe today?",
"How's your energy level today?",
"How's everything with you today?",
"How have you been feeling today?",
"How's your state of mind today?"] 



sadfeeling=["sad","low","lack of energy","guilty","failure","worthless","lack of energy","tired","to cry","crying","to suicide","loss of interest","alone","depressed"]

happyfeeling=["feeling joy","happy","good","very happy","joyfull"]

feeling=["feeling joy","good","happy","very happy","joyfull","sad","low","lack of energy","guilty","failure","worthless","lack of energy","tired","to cry","crying","to suicide","loss of interest","alone","depressed"]



santawna=[
    "i am here for you",
    "i am with you",
    "i am always with you",
    "i am always there for you",
    "i am always there",
    "you can share with me",
    "you can ask me",
    "you can tell me"
]


problems=[
"Personal Struggles",
"Career and Financial Pressures",
"Relationships and Social Pressures",
"Existential and Psychological Factors",
"External Factors",
"Emotional Reasons for Feeling Alone",
"Physical and Mental Exhaustion",
"Suicidal thoughts"
]



personal_struggles=[
"Are you suffering with loneliness or Isolation - Feeling disconnected from friends, family, or society.",
"Did you had Breakup or Divorce - The end of a relationship can be emotionally devastating.",
"Are you feeling of Grief and Loss - Losing a loved one, a pet, or even a job can trigger deep sadness.",
"Do you have Health Issues - Chronic illness, injury, or mental health struggles can be overwhelming.",
"Are you feeling Low Self-Esteem - Feeling inadequate or not good enough."
]

career_and_financial_pressures=[
"Job Loss or Career Stagnation - Struggling to find work or feeling stuck in an unfulfilling job.",
"Financial Stress - Debt, inability to provide for family, or financial instability.",
"Work Burnout - Feeling overworked, unappreciated, or exhausted from professional demands."
]

relationships_and_social_pressures=[
"Family Issues - Conflict with parents, siblings, or children.",
"Feeling Unappreciated - Lack of acknowledgment in relationships, at work, or in personal efforts.",
"Difficulty Expressing Emotions - Societal pressure to stay strong and not show vulnerability.",
"Betrayal or Trust Issues - Being hurt by close friends, partners, or colleagues."
]

existential_and_psychological_factors=[
"Lack of Purpose - Feeling like life lacks meaning or direction.",
"Midlife Crisis - Questioning life choices and accomplishments.",
"Regret Over Past Decisions - Feeling stuck due to mistakes or missed opportunities.",
"Feeling Trapped in Routine - Life feeling monotonous and unchanging."
]

external_factors=[
"World Events and News - Wars, economic instability, and global crises can weigh heavily.",
"Weather and Seasonal Depression - Lack of sunlight or long winters can affect mood.",
"Substance Abuse - Alcohol or drug dependency can lead to emotional struggles."
]

emotional_reasons_for_feeling_alone=[
"Lack of Deep Connections - Having many acquaintances but no real emotional support.",
"Strained Relationships - Conflicts with family, friends, or a romantic partner.",
"Social Isolation - Spending too much time alone due to work, circumstances, or personal choice.",
"Breakup or Divorce - Losing a romantic partner can create deep loneliness.",
"Feeling Unheard or Misunderstood - Even when surrounded by people, not feeling truly seen or valued.",
"Societal Pressure on Men - Expectations to be strong and not express vulnerability.",
"Betrayal or Abandonment - Losing trust in someone who was once a close part of life.",
"Grief and Loss - Losing a loved one, pet, or something meaningful.",
"Midlife Crisis - Feeling like time is passing without achieving personal fulfillment."
]
    
physical_and_mental_exhaustion=[
"Work Burnout - Long hours, high stress, and lack of rest.",
"Financial Stress - Worrying about money can be mentally exhausting.",
"Lack of Sleep - Poor sleep quality leads to both mental and physical exhaustion.",
"Health Issues - Chronic pain, illness, or fatigue disorders.",
"Poor Diet and Lack of Exercise - Unhealthy habits draining energy.",
"Mental Overload - Constant stress, overthinking, and anxiety.",
"Carrying Too Many Responsibilities - Juggling work, family, and personal struggles alone.",
"Lack of a Break or Vacation - Never taking time to recharge.",
"Depression or Anxiety - Mental health struggles can make everything feel overwhelming."
]

suicidal_thoughts=[
"Emotional Pain and Mental Health Struggles",
"Depression - Persistent feelings of sadness, hopelessness, and worthlessness.",
"Anxiety and Overwhelm - Feeling constantly on edge, exhausted, or unable to cope.",
"Trauma and PTSD - Unresolved past trauma or abuse affecting daily life.",
"Loneliness and Isolation - Feeling disconnected from others or believing no one cares.",
"Guilt or Shame - Over past mistakes, failures, or personal struggles.",
"Relationship and Social Struggles",
"Breakup, Divorce, or Rejection - Losing a partner or feeling unworthy of love.",
"Family Problems - Conflict, neglect, or feeling like a burden.",
"Loss of a Loved One - Grieving and feeling unable to cope with the pain.",
"Betrayal or Abandonment - Losing trust in someone once deeply valued.",
"Lack of Emotional Support - Feeling like no one understands or listens.",
"Financial and Career Pressures",
"Job Loss or Career Failure - Struggling with unemployment or feeling useless.",
"Financial Stress - Debt, bankruptcy, or being unable to provide for family.",
"Work Burnout - Feeling exhausted, undervalued, or trapped in a stressful job.",
"Feeling Like a Failure",
"Loss of Direction",
"Midlife Crisis",
"Physical Health and Addiction",
"External and Societal Pressures:"
]


happy=[
"That's great to hear! What's making you happy today?",
"Awesome! Your happiness is contagious!",
"Love that for you! Hope it lasts all day.",
"That's the best news I've heard today.",
"You deserve it! Anything special happening?",
"Really? Tell me more!",
"What's going right today?",
"That's wonderful—what's the secret?",
"Spreading joy, I see!",
"Should I be happy too, or is this an exclusive deal?"
]


happyreaction=[
"I'm so glad to hear that!",
"That's wonderful — you deserve it!",
"That makes me happy too!",
"Keep smiling! You've earned it.",
"I love seeing you like this!"
"What's got you feeling so good?",
"Tell me more — I want to hear all about it!",
"That's great! What's the reason behind the smile?",
"Something special happen today?"
"Uh-oh, who made you smile like that?",
"Careful, your happiness is showing!",
"Pass some of that joy over here!"
]