from datetime import datetime
import subprocess
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

Query = r.recognize_google(audio)
print(Query)


def get_app(Q):
    if Q == "time":
        print((datetime.now()))
    elif Q == "notepad":
        subprocess.call(["Notepad.exe"])
    elif Q == "calculator":
        subprocess.call(["calc.exe"])
    elif Q == "stikynot":
        subprocess.call(["StikyNot.exe"])
    elif Q == "shell":
        subprocess.call(["powershell.exe"])
    elif Q == "paint":
        subprocess.call(["mspaint.exe"])
    elif Q == "cmd":
        subprocess.call(["cmd.exe"])
    elif Q == "browser":
        subprocess.call(["C:\Program Files\Internet Explorer\iexplore.exe"])
    else:
        print("Sorry ! Try Again")
    return


get_app(Query)
