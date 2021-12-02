import pyttsx3 as ts
import speech_recognition as ani
import datetime
from time import ctime
import webbrowser
import os
import subprocess
import pyjokes
from youtube import *
from classes import *

engine = ts.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

gs = ani.Recognizer()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def record():
    with ani.Microphone() as inp:
        gs.energy_threshold = 10000
        gs.adjust_for_ambient_noise(inp, 1.2)
        print("Listening...")
        out = gs.listen(inp)
        store = ''
        try:
            print('Recognizing...')
            store = gs.recognize_google(out)
            print(store)
        except ani.UnknownValueError:
            print('sorry didnt get that')
        except ani.RequestError:
            print('service error')

    return store


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 16:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am your voice assistant")
    print('What should i call you ?')
    speak('what should i call you ?')
    name = record().lower()
    print('Hello '+name)
    speak('hello  ' + name)
    print("How can i help you?")
    speak("How can i help you?")


def respond(store):

    if 'what is your name' in store:
        speak('Well I do not have any name my creaters forget to give me name in hurry')
    elif "how are you" in store:
        speak("I am having a good day sir")
        speak("what can I do for you sir??")

    elif 'time' in store:
        print(ctime())
        speak(ctime())

    elif 'hey good morning' in store:
        print('Good morning sir.')
        speak('Good morning sir.')

    elif 'good evening' in store:
        print('Good Evening sir.')
        speak('Good Evening sir.')

    elif 'good night' in store:
        print('Good Night Sweet Dreams...')
        speak('Good Night Sweet Dreams...')

    elif 'open lpu live' in store:
        print('you are redirecting to LPU LIVE')
        speak('you are redirecting to LPU LIVE')
        webbrowser.open("lpulive.lpu.in")

    elif 'open o a s' in store:
        print('you are redirecting to OAS')
        speak('you are redirecting to OAS')
        webbrowser.open("oas.lpu.in/")

    elif 'open u m s' in store:
        print('you are redirecting to UMS')
        speak('you are redirecting to UMS')
        webbrowser.open("ums.lpu.in/lpuums/")

    elif 'open my class' in store:
        print('you are redirecting to My Class')
        speak('you are redirecting to My Class')
        webbrowser.open("myclass.lpu.in/")

    elif 'schedule' in store:
        print('you are redirecting to My Class')
        speak('you are redirecting to My Class')
        check = myclass()
        check.schedule()

    elif 'open youtube' in store:
        print('you are redirecting to youtube')
        speak('you are redirecting to youtube')
        webbrowser.open("youtube.com")

    elif 'play video on youtube' in store:
        print('Name of the video you want to play')
        speak('name of the video you want to play')
        query = record().lower()
        print("playing "+query+" on youtube")
        speak("playing" + query+" on youtube")
        assist = music()
        assist.play(query)

    elif 'search' in store:
        print('What you want to search')
        speak('what you want to search')
        query = record().lower()
        webbrowser.open("https://www.google.co.in/search?q=" + query)

    elif 'play music' and 'play song' in store:
        print('Name the platform where you want to listen')
        speak('name the platform where you want to listen')

        say = record().lower()
        if 'spotify' in say:
            print('Name of the song you want to play')
            speak('name of the song you want to play')
            query = record().lower()
            webbrowser.open("https://open.spotify.com/search/" + query)

        elif 'jio saavan' in say:
            print('Name of the song you want to play')
            speak('name of the song you want to play')
            query = record().lower()
            webbrowser.open("https://www.jiosaavn.com/search/" + query)

        elif 'gaana' in say:
            print('Name of the song you want to play')
            speak('name of the song you want to play')
            query = record().lower()
            webbrowser.open("https://gaana.com/search/" + query)

        elif 'joke' in store:
            joke = pyjokes.get_joke(language='en', category='all')
            print(joke)
            speak(joke)

        elif 'open chrome' in store:
            print('opening chrome...')
            speak('opening chrome')
            dir = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(dir)
            os.system(dir)
            subprocess.Popen(dir)
            subprocess.call(dir)


greet()
store = record().lower()
respond(store)
