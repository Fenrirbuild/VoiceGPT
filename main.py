import speech_recognition as sr
import win32com.client
import os
import webbrowser
import openai
import datetime
from config import apikey
import random

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Rate = -2


# todo: Wrap this in a catch exception
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for prompt: {prompt} \n****************\n\n "

    response = openai.Completion.create(
        model="text-davinci-003",  # This is legacy from 2024 use a different model
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    # with open(f"prompt - {random.randint(1, 123456789)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('AI')[1:]).strip() }.txt", "w") as f:
        f.write(text)


def say(text):
    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1  (it is 0.8 by default, see if there is a differnce)
        audio = r.listen(source)
        try:
            print("Understanding...")
            query = r.recognize_google(audio, language="en-US")  # Check other languages if this works....
            print(f"user said : {query}")
            return query
        except Exception as e:
            return "Something unrecognizable"  # Either return it in a voice or print it, see if it works first


if __name__ == '__main__':
    print('PyCharm')
    say("Hello and welcome")
    while True:
        print("listening...")
        query = takeCommand()
        sites = [["youtube", "https://Youtube.com"], ["wikipedia", "https://wikipedia.com"],
                 ["google", "https://google.com/no"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])

        if "Play Music".lower() in query.lower():
            musicPath = "C:/Users/anas_/Downloads/Songs/Sun-Re.mp3"
            if os.path.exists(musicPath):
                os.startfile(musicPath)
            else:
                print("Music file not found, try searching for another name")
            #   say("Music file not found, try searching for another name")
            # The voice can be annoying stick to print
        # say(query)
        if "What is the time".lower() in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strfTime} ")

        if "Open chrome".lower() in query.lower():
            os.system(
                r'"C:\Program Files\Google\Chrome\Application\chrome.exe"')  # Use double quotes for similar paths so cmd treats it as a single paath even with spaces

        if "Use AI".lower() in query.lower():
            ai(prompt=query)
