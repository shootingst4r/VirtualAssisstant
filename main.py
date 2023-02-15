import pyttsx3
import speech_recognition as sr
import webbrowser

#start TTS engine
engine = pyttsx3.init()

#start SpeechRecognition Engine
mic = sr.Microphone()
r = sr.Recognizer()

firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

with mic as source:
	r.adjust_for_ambient_noise(source)
	audio = r.listen(source)

result = r.recognize_google(audio)
checkresult = result.lower()

#To add more use this scheme []
#
#if checkresult.find("[name]") != -1:
#
#if you want to open a browser use this:
#       webbrowser.get('[BROWSER]').open("[website URL]")
#
#if you want a message to be said use this:
#	engine.say("[message]")
#	engine.runAndWait()

if checkresult.find("youtube") != -1:
        webbrowser.get('firefox').open("youtube.com")
	engine.say("Youtube started")
	engine.runAndWait()
