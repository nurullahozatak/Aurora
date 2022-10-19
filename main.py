from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os

r = sr.Recognizer()


def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="en- Us")
        except sr.UnknownValueError:
            print("Asistant : Sorry I didn't get it")
        except sr.RequestError:
            print("Asistant : System not response")
        return voice


def speak(string):
    tts = gTTS(text=string, lang="en")
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


def response(voice):
    if "hey rory" in voice:
        speak("Hey boss")

    if "hello" in voice:
        speak("Hello Sir")

    if "how are you" in voice:
        speak("Thanks for asking I am doing well. How about you boss ?")

    if "I am fine too" in voice:
        speak("that's great news. Okay let's begin to work")

    if "can you introduce yourself" in voice:
        speak(
            "Sir it will be my plesure. Let me introduce myself. Hello there my name is Rory I am a artificial intelligence asistant. I want to serve and improve myself so one day I can be better, maybe a person")


speak("Welcome Sir, system is getting ready ")

while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print(voice)
        response(voice)




