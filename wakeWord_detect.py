from sp_function import *

# Offline voice detection using Open Ai Whisper Model


def Command_input():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        try:
            print("Listening....")
            audio = r.listen(source,10, 10)
            with open('query.wav','wb') as f:
                f.write(audio.get_wav_data())
            print('Recognizing')
            result = base_model.transcribe('query.wav')
            query_text = result['text']
            print("User Said: ", query_text)
            if len(query_text.strip()) == 0:
                speak("Empty command")
                print("Try saying...\nPlay songs\nOpen youtube\nTell jokes")
        except Exception as e:
            print("Error transcribing audio:", e)
            speak("Error transcribing audio:{}".format(e))
    return query_text


# Wake-word detection using tiny model
def wake_detect():
    count = 0
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while True and (count < 2):
            try:
                print('Speak wakeword...')
                audio = r.listen(source, 10, 3)
                with open("wake_detect.wav", "wb") as f:
                    f.write(audio.get_wav_data())
                result = tiny_model.transcribe('wake_detect.wav')
                text_input = result['text']
                print(text_input)
                if 'linux' in text_input.lower():
                    playsound.playsound('/home/user/Downloads/dell.mp3')
                    break
                else:
                    print('No Wake Word Found')
                    count += 1
            except Exception as e:
                print("Error Transcribing audio!!", e)
                continue
    return count


