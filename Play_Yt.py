import pywhatkit
from sp_function import *
import os


def play_on_yt():
    print("Linux Assistant: Shall I play something on youtube")
    g_speak("Shall I play something on youtube")
    y = takeCommand()
    if 'yes' in y.lower():
        print("Linux Assistant: What would you like to see or Listen?")
        g_speak("What would you like to see or Listen?")
        yt = takeCommand()
        yt.lower()
        yt = yt.replace("play", "")
        print(f"Linux Assistant: Playing {yt} on youtube")
        g_speak(f"playing {yt} on youtube")
        pywhatkit.playonyt(yt)


def stop_yt():
    print("Linux Assistant: Closing youtube")
    g_speak("closing youtube")
    os.system("sleep 0.5 && xdotool key 'Control+w'")
