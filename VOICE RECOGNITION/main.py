import pyttsx3 as p
from selenium_web import infow
from time import sleep
from YT_audio import music
from News import *
import randfacts
# from joke import *


# convert speech to text - using speech Recognition
import speech_recognition as sr

# create an instace of speech Recognizer class
r = sr.Recognizer()

# initialize a p instance in class. init
engine = p.init()

# get voice properties
rate = engine.getProperty('rate')

# change rate of the sound
engine.setProperty('rate', 130)

# see what voices the library provides for us
voices = engine.getProperty('voices')
# print(voices)

engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("Hello , I'm your voice assistant. How are you")

# speech to text
with sr.Microphone() as source:
    # recognize properties such as threshold properties and ambient noice
    # increasing threshold increases the sensitivity
    r.energy_threshold = 10000

    # it filters background noise
    r.adjust_for_ambient_noise(source, 1.2)

    print("listening")
    audio = r.listen(source)
    # convert to text using recognize google api
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak("I am also having a good day")
speak("what can I do for you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print('listening...')
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" and "need" and "some" in text2:

    # make instance of class
    speak("you need information related to which topic?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print('listening...')
        audio = r.listen(source)
        infor = r.recognize_google(audio)

    speak("searching {} in Wikipedia".format(text2))
    assist = infow()
    assist.get_info(infor)
    sleep(100)

elif "play" and "video" in text2:
    speak("you want me to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print('listening...')
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    speak("Playing {} on youtube".format(vid))
    assist = music()
    assist.play(vid)
    sleep(10)

elif "news" and "read" in text2:
    speak("Sure! Here is the latest news")
    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" or "facts" in text2:
    speak("Sure! Here is the random fact")
    x = randfacts.getFact()
    print(x)
    speak("Did you know that, " + x)

# elif "joke" or "jokes" in text2:
#     speak("Sure! Get ready for some laughs")
#     jokeList=joke()
#     print(jokeList[0])
#     speak(jokeList[0])
#     print(jokeList[1])
#     speak(jokeList[1])

print('done')
