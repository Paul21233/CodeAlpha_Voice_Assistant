import speech_recognition as sr
import pyttsx3 as tts
import os
import datetime
import time
import subprocess
import wikipedia
import webbrowser
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import sys
import tkinter as tk
import threading


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            com = recognizer.recognize_google(audio)
            print(f"You said: {com}")
            return com
        except sr.UnknownValueError:
            print("Sorry, I could not understand audio")
            return ""
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return ""


def speak(text):
    engine = tts.init()
    engine.say(text)
    engine.runAndWait()


def command(com):
    if 'open_browser' in com:
        speak("Opening browser...")
        webbrowser.open("https://google.com")
    elif 'time' in com:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")
    elif 'date' in com:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"The date is {date}")
    else:
        speak("I'm not sure how to help with that")


def main():
    while True:
        com = listen().lower()
        if command:
            command(com)


if __name__ == "__main__":
    main()
