import pyttsx3 as p
import speech_recognition as sr
import pyaudio as pa


engine  = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
#print(voices)

def speak(text):
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()

speak("Hello Sir. I am your AI Assistant. How are you")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print('listening')
    audio = r.listen(source)
    text = r.recognize_google(audio)


if "what" and "about" and "you" in text:
    speak("I am having a good day sir!")
speak("what can I do for you?")