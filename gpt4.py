from gpt4all import GPT4All
from sp_function import *
# **WE CAN DOWNLOAD THE FALCON OPEN-SOURCE LLM IF RAM SPACE > 8GB**
# model = GPT4All('falcon-7b-Q4_0GGUF.gguf')


def get_from_mini(text):
    model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
    output = model.generate(text, max_tokens=120)
    g_speak("The answer is ")
    print(f"Linux Assistant:{output}")


def give_reply(text):
    text = text + ". Imagine you are an assistant and write a short common human language "
    model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
    output = model.generate(text, max_tokens=120)
    g_speak(output)
    return output
