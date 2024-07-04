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


def weather(city_name):
    api_key = "2db14941b6964b98a42141601240307"
    base_url = "http://api.weatherapi.com/v1/current.json"
    complete_url = f"{base_url}?key={api_key}&q={city_name}"

    response = requests.get(complete_url)
    data = response.json()

    if "error" not in data:
        current_temp = data['current']['temp_c']
        current_humid = data['current']['humidity']
        weather_description = data['current']['condition']['text']
        speak(f"Temperature is {current_temp} degree celsius, humidity is {current_humid} percent, and weather is described as {weather_description}.")
        print(f"Temparature: {current_temp} °C\n, Humidity: {current_humid}%\n, and Weather details: {weather_description}.")
    else:
        speak("City not found. Please try again.")
        print("City not found. Please try again.")

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
            speak("what is the city")
            city_name = takeCommand()
            weather(city_name)


if __name__ == '__main__':
    main()
