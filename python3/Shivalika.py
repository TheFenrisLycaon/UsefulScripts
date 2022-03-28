import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    speak("I am Shivalika, How Can I Help You?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language="en-in")
        print(("User Said:", query))
    except Exception as e:
        print(e)
        print("Say that again...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=5)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "play music" in query:
            music_dir = "E:\\Media\\Audio\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            y = random.randint(1, 854)
            os.startfile(os.path.join(music_dir, songs[y]))
