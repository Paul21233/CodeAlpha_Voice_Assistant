import speech_recognition as sr
import pyttsx3 as tts
import os
import datetime
import time
import subprocess
import wikipedia
import webbrowser
import wolframalpha
import json
import requests
import sys
import tkinter as tk
import threading
import platform


def get_engine():
    system = platform.system()
    if system == 'Windows':
        return tts.init('sapi5')
    elif system == 'Darwin':
        return tts.init('nss')
    else:
        return tts.init('espeak')


def get_engine():
    system = platform.system()
    if system == 'Windows':
        return tts.init('sapi5')
    elif system == 'Darwin':
        return tts.init('nss')
    else:
        return tts.init('espeak')


def speak(text):
    engine = get_engine()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


def ask():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello Banika, Good Morning")
        print("Hello Banika, Good Morning")
    elif 12 <= hour < 18:
        speak("Hello Banika, Good Afternoon")
        print("Hello Banika, Good Afternoon")
    else:
        speak("Hello Banika, Good Evening")
        print("Hello Banika, Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please tell me how can I help you...")
        audio = r.listen(source)
        try:
            statement = r.recognize_google(audio, language='en-us')
            print(f"user said: {statement}\n")
        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


def main():
    print("Loading your personal assistant...")
    speak("Loading your personal assistant...")
    ask()

    while True:
        speak("How can I help you?")
        statement = takeCommand().lower()
        if statement == "none":
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak("your personal assistant is shutting down")
            print("your personal assistant is shutting down")
            sys.exit()

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is opening now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("your mail is opening now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("google is opening now")
            time.sleep(5)

        elif 'wikipedia' in statement:
            speak('Searching...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'time' in statement:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")

        elif 'ask' in statement:
            speak('I can answer to computational questions. Feel free to ask me')
            question = takeCommand()
            app_id = "paste your unique ID here"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'weather' in statement:
            api_key = "Apply your unique id"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            a = response.json()
            if a["cod"] != "404":
                b = a["main"]
                current_temp = b["temp"]
                current_humid = b["humidity"]
                c = a["weather"]
                weather_description = c[0]["description"]
                speak(" Temperature in kelvin unit is " + str(current_temp) +
                      "\n humidity in percentage is " +
                      str(current_humid) +
                      "\n description " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " + str(current_temp)
                      + "\n description " + str(weather_description) +
                      "humidity (in percentage) = " +
                      str(current_humid))
            else:
                speak("City not found. Please try again.")
                print("City not found. Please try again.")


if __name__ == '__main__':
    main()
