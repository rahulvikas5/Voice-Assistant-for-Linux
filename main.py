import webbrowser
import os
from PIL import Image
import time
from pynput.keyboard import Controller
import warnings
import pyjokes
import wikipedia
import shutil
import Play_Yt
import gpt4
import news
import takeselfie
import wlf
import openai_ap
from sp_function import *
import sounddevice
from Data import *
import weather

warnings.filterwarnings("ignore", message='FP16 is not supported on CPU; using FP32 instead')
keyboard = Controller()


def username():
    print("Say your name to wake up!")
    uname = takeCommand()
    if uname == 'None':
        print("Linux Assistant: No name is detected. Can i call you mine?")
        g_speak("No name is detected. Can I call you mine?")
    else:
        wishMe()
        g_speak(uname)
        print("**************** Welcome ", uname, "******************")
        g_speak("How can i Help you?")


if __name__ == '__main__':
    username()
    print("\n")
    print("Try these Commands!! \n"
          "1.Search topics\n"
          "2.Open/ Close applications\n"
          "3.Entertain\n"
          "4.System Control (Volume control etc..)\n"
          "5.Ask jokes\n"
          "6.Ask any Query/Doubt/Math Calculations etc..")
    while True:
        text = takeCommand()
        if 'time' in text.lower():
            time = datetime.datetime.now().strftime("%H:%M")
            print("Linux Assistant :"+time)
            g_speak(f"the time is {time}")

        #   --------------general_use()-----------------
        elif 'good morning' in text.lower():
            print("Linux Assistant : Good Morning!")
            g_speak("Good Morning")
        elif 'how are you' in text.lower():
            print("Linux Assistant : I am fine, Thank you. How are you?")
            g_speak("I am fine, Thank you")
            g_speak("How are you?")
        elif 'who are you' in text.lower():
            print("Linux Assistant : I am your personal assistant")
            g_speak("I am your personal assistant")
        elif 'who created you' in text.lower():
            print("The team of Rahul Rohith and Vijay created me")
            g_speak("The team of Rahul Rohith and Vijay created me")
        elif 'fine' in text.lower():
            print("Linux Assistant : It's good to know that you are fine")
            g_speak("It's good to know that your fine")
            print("Linux Assistant : How can I assist you?")
            g_speak("How can I Assist you")
        elif 'joke' in text.lower():
            j = pyjokes.get_joke()
            print(j)
            g_speak(j)

        # ----------------------Camera-------------------------
        elif 'take selfie' in text.lower():
            print("Linux Assistant : Please smile:)")
            takeselfie.takeselfie()
        elif 'show selfie' in text.lower():
            print("Linux Assistant : Opening recent selfie")
            with Image.open('/home/user/VA_Project/Voice Assistant/selfie.jpg') as img:
                img.show()

        # --------------------Screenshot-----------------------
        elif 'take screenshot' in text.lower():
            print("Linux Assistant : Screenshot captured")
            os.system("gnome-screenshot --file=screenshot.jpg")
        elif 'show screenshot' in text.lower():
            print("Linux Assistant : Opening recent screenshot")
            with Image.open('/home/user/VA_Project/Voice Assistant/screenshot.jpg') as img:
                img.show()

        # -------------------Volume up/down---------------------

        elif 'volume up' in text.lower():
            os.system("amixer -D pulse sset Master 10%+")
        elif 'volume down' in text.lower():
            os.system("amixer -D pulse sset Master 10%-")
        elif 'mute' in text.lower():
            os.system("amixer -D pulse sset Master 0%")

        # -------------------Page up/down-----------------------
        elif 'scroll up' in text.lower():
            os.system("sleep 0.5 && xdotool key 'Prior'")
        elif 'scroll down' in text.lower():
            os.system("sleep 0.5 && xdotool key 'Next'")

        # ----------------Computer power commands----------------
        elif 'system sleep' in text.lower():
            print("Linux Assistant : System is about to sleep 3..2..1")
            time.sleep(3)
            os.system("systemctl suspend")
        elif 'system power off' in text.lower():
            print("Linux Assistant : System is shutting down...")
            time.sleep(3)
            os.system("systemctl poweroff")
        elif 'system restart' in text.lower():
            print("Linux Assistant : System is about to restart...")
            time.sleep(3)
            os.system("systemctl reboot -i")
        elif 'system log out' in text.lower():
            print("Linux Assistant : User is logging out...")
            time.sleep(3)
            os.system("systemctl logout")

        # --------------------Bluetooth/Wi-Fi---------------------
        elif 'enable bluetooth' in text.lower():
            print("Linux Assistant : Bluetooth is turned on")
            g_speak("Bluetooth is turned on")
            os.system("rfkill unblock bluetooth")
        elif 'disable bluetooth' in text.lower():
            print("Linux Assistant : Bluetooth is turned off")
            g_speak("Bluetooth is turned off")
            os.system("rfkill block bluetooth")
        elif 'enable Wi-Fi' in text.lower():
            print("Linux Assistant : Wi-Fi is turned on")
            g_speak("Wi-Fi is turned on")
            os.system("nmcli radio wifi on")
        elif 'disable Wi-Fi' in text.lower():
            print("Linux Assistant : Wi-Fi is turned off")
            g_speak("Wi-Fi is turned off")
            os.system("nmcli radio wifi off")

        # ------------------Write/show notes----------------------
        elif 'write notes' in text.lower():
            print("Linux Assistant : What do you want me to write?")
            g_speak("what do you want me to write?")
            note = takeCommand()
            file = open('demonotes.txt', 'w')
            file.write(note)
        elif 'show notes' in text.lower():
            print("Showing Notes")
            g_speak("Showing Notes")
            file = open('demonotes.txt', 'r')
            os.system("gedit demonotes.txt")
            print("Linux Assistant :", file.read())

        # --------------------Location----------------------------
        elif 'where is' in text.lower():
            text = text.replace("where is", "")
            location = text
            try:
                g_speak(location)
            except Exception as l:
                continue
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        # ------------------Search command------------------------
        elif 'search' in text.lower():
            text = text.replace("search", "")
            webbrowser.open("https://www.google.co.in/search?q=" + text)

        # -------------------Using Wikipedia----------------------

        elif 'wikipedia' in text.lower():
            print('Linux Assistant : Searching Wikipedia...')
            g_speak('Searching Wikipedia...')
            text = text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=2)
            print("Linux Assistant : According to Wikipedia")
            g_speak("According to Wikipedia")
            print("Linux Assistant : "+results)
            g_speak(results)

        # ------------------WEATHER-------------------------
        elif 'weather' in text.lower():
            weather.get_weather()
        elif 'news' in text.lower():
            news.get_news()

        # -----------------Wolframalpha-----------------------
        elif text.startswith(que):
            try:
                wlf.get_ans(text)
            except Exception as w:
                print('Linux Assistant : Results got from using the LLM\n')
                # Ocra Mini LLM function
                gpt4.get_from_mini(text)

        # ----------------- ChatGPT ----------------------------
        elif 'using chat gpt' in text.lower():
            try:
                openai_ap.gpt_getanswer(text)
            except Exception as c:
                print("Linux Assistant: Looks like you have exceeded your free quota of ChatGPT or your API key isn't valid.")
                g_speak("Looks like you have exhausted your free quota of ChatGPT or your API key isn't valid.")
        # ----------------Closing Applications------------------
        elif 'close visual studio' in text.lower():
            os.system("killall code")
        elif 'close chrome' in text.lower():
            os.system("killall chrome")
        elif 'close vlc' in text.lower():
            os.system("killall vlc")

        # -----------------Tab open/close----------------------------
        elif 'new tab' in text.lower():
            os.system("sleep 0.5 && xdotool key 'Control+t'")
        elif 'close tab' in text.lower():
            os.system("sleep 0.5 && xdotool key 'Control+w'")
        elif 'entertain me' in text.lower():
            Play_Yt.play_on_yt()
        elif 'i am bored' in text.lower():
            Play_Yt.play_on_yt()
        elif 'stop youtube' in text.lower():
            Play_Yt.stop_yt()
        elif 'close youtube' in text.lower():
            Play_Yt.stop_yt()
        elif text.lower() in terminate:
            print("Linux Assistant : Thanks for giving me your time")
            g_speak("Thanks for giving me your time")
            exit()
        elif 'wait' in text.lower():
            time.sleep(10)
        else:
            counting = 0
            for site in sites:
                if f'open {site}'.lower() in text.lower():
                    print(f"Linux Assistant: Opening {site} ")
                    g_speak(f'Opening {site} ')
                    webbrowser.open(sites[site])
                    counting += 1

            for m in media:
                if f'play {m}'.lower() in text.lower():
                    print("Linux Assistant: Playing {}".format(m))
                    g_speak(f'Playing {m} ')
                    if m == 'songs':
                        os.system("nvlc venv/Songs --playlist-autostart")
                    elif m == 'music':
                        os.system("nvlc venv/Songs --playlist-autostart")
                    elif m == 'movies':
                        os.system("mplayer -fs %s venv/movie.mp4")
                    counting += 1

            for a in apps:
                if f'open {a}'.lower() in text.lower():
                    print(f"Linux Assistant: opening {a}")
                    g_speak(f'opening {a}')
                    os.system(f'{apps[a]}')
                    counting += 1

            for grat in grati:
                if f'{grat}'.lower() in text.lower():
                    print(f"Linux Assistant:  {grati[grat]}")
                    g_speak(f'{grati[grat]}')
                    counting += 1
            if counting > 0:
                continue
            else:
                try:
                    op = gpt4.give_reply(text)
                    if len(op) > 0:
                        print(f"Linux Assistant:{op}")
                except Exception as x:
                    continue


