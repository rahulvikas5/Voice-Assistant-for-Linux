import pyttsx3
import speech_recognition as sr
import whisper
import playsound
import datetime
import gtts
from playsound import playsound
r = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty("voices")
engine.setProperty('rate', rate-80)
engine.setProperty('voice', 'english_rp+f3')
tiny_model = whisper.load_model('tiny')
base_model = whisper.load_model('base')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Voice recognition using Google SR
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 10, 10)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        if len(query.strip()) == 0:
            g_speak("Empty command")

    except Exception as e:
        print(e)
        print("Linux Assistant: I didn't recognize your voice.")
        g_speak("I didn't Recognize your voice.")
        return "None"

    return query


def g_speak(text):
    t1 = gtts.gTTS(text)
    t1.save("output.mp3")
    playsound("output.mp3")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        print("Linux Assistant: Welcome!!!!")
        g_speak("Good Morning !")

    elif 12 <= hour < 16:
        print("Linux Assistant: Welcome!!!!")
        g_speak("Good Afternoon !")

    else:
        print("Linux Assistant: Welcome!!!!")
        g_speak("Good Evening !")
    print("I am your personal assistant.")
    g_speak("I am your Assistant")