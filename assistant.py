import speech_recognition as sr
import pyttsx3
import datetime
import time
from time import ctime
import pywhatkit
import pyjokes
import os
import subprocess
import webbrowser
from classes import *

engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", 180)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

listener = sr.Recognizer()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def record():
    with sr.Microphone() as inp:
        listener.energy_threshold = 10000
        listener.adjust_for_ambient_noise(inp, 1.2)
        print("Listening...")
        out = listener.listen(inp)
        command = ""
        try:
            print("Recognizing...")
            command = listener.recognize_google(out)
            print("You: " + command)
        except sr.UnknownValueError:
            print("sorry didnt get that")
        except sr.RequestError:
            print("service error")

    return command.lower()


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 16:
        speak("good afternoon")
    elif hour >= 16 and hour < 0:
        speak("good evening")
    print("What should i call you ?")
    speak("what should i call you ?")
    name = record()
    print("Hello" + name)
    speak("Hello " + name)
    print("How can I help ?")
    speak("How can I help ?")


def respond(command):

    # Conversation

    if "hi" and "hello" in command:
        speak("Hi, it's really good to hear from you! I hope you and your loved ones are safe and healthy")

    elif "time" in command:
        print(ctime())
        speak(ctime())

    elif "name" in command:
        speak("Well I do not have any name my creaters forget to give me name in hurry")

    elif "who are you" and "what you can do" in command:
        speak("I am your assistant. I can look up answers for you, or help you to play videos. If you need anything just ask, your wish is my command")

    elif "old" and "age" in command:
        speak("Well, I'm still pretty new.")

    elif "how are you" in command:
        speak("I'm fine. You're very kind to ask especially in these tempestuous times")

    elif "are you single" in command:
        speak("I am in a relationship with your wifi")

    # Activity

    elif "search" in command:
        print("To find info about somthing, just ask")
        speak("To find info about somthing, just ask")
        query = record()
        url = "https://www.google.co.in/search?q=" + query
        webbrowser.open(url)
        speak("Here what I found" + query)

    elif "tell me" in command:
        query = command.replace("tell me", "")
        url = "https://www.google.co.in/search?q=" + query
        webbrowser.open(url)
        speak("Here what I found" + query)

    elif "find location" in command:
        print("Sure, tell me the name of location.")
        speak("Sure, tell me the name of location.")
        query = record()
        url = "https://google.nl/maps/place/" + query
        webbrowser.open(url)
        speak("Here what I found" + query)

    elif "open youtube" in command:
        print("Opening Youtube")
        speak("Opening Youtube")
        url = "https://www.youtube.com"
        webbrowser.open(url)

    elif "open lpu live" in command:
        print("you are redirecting to LPU LIVE")
        speak("you are redirecting to LPU LIVE")
        url = "https://lpulive.lpu.in/login"
        webbrowser.open(url)

    elif "open o a s" in command:
        print("you are redirecting to OAS")
        speak("you are redirecting to OAS")
        url = "https://oas.lpu.in/"
        webbrowser.open(url)

    elif "open u m s" in command:
        print("you are redirecting to UMS")
        speak("you are redirecting to UMS")
        url = "https://ums.lpu.in/lpuums/LoginNew.aspx"
        webbrowser.open(url)

    elif "open my class" in command:
        print("you are redirecting to My Class")
        speak("you are redirecting to My Class")
        url = "https://myclass.lpu.in/"
        webbrowser.open(url)

    elif "open calculator" in command:
        print("Opening Calculator")
        speak("Opening Calculator")
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')

    elif "open chrome" in command:
        print("Opening Chrome")
        speak("Opening Chrome")
        subprocess.Popen(
            'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')

    elif "joke" in command:
        speak(pyjokes.get_joke())

    # Play

    elif "play video on youtube" in command:
        print("Name of the video you want to play")
        speak("Name of the video you want to play")
        query = record()
        print("Playing "+query+" on youtube")
        speak("Playing" + query+" on youtube")
        pywhatkit.playonyt(query)

    elif "play" in command:
        query = command.replace("play", "")
        print("Playing "+query+" on youtube")
        speak("Playing " + query+" on youtube")
        pywhatkit.playonyt(query)

    elif "play songs" and "play music" in command:
        print("Name the platform where you want to play")
        speak("Name the platform where you want to play")

        say = record()
        if "spotify" in say:
            print("Name of the song you want to play")
            speak("name of the song you want to play")
            query = record()
            webbrowser.open("https://open.spotify.com/search/" + query)

        elif "jio saavan" in say:
            print("Name of the song you want to play")
            speak("name of the song you want to play")
            query = record()
            webbrowser.open("https://www.jiosaavn.com/search/" + query)

        elif "gaana" in say:
            print("Name of the song you want to play")
            speak("name of the song you want to play")
            query = record()
            webbrowser.open("https://gaana.com/search/" + query)

        # Automation

        elif "schedule" in command:
            print("you are redirecting to My Class")
            speak("you are redirecting to My Class")
            check = myclass()
            check.schedule()

        elif "exit" in command:
            speak("Alright! Thankyou for using me.")
            exit()

        else:
            speak("Please say it again.")


time.sleep(1)
greet()
while True:
    command = record()
    respond(command)
