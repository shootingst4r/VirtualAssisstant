import pyttsx3
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init()

mic = sr.Microphone()
r = sr.Recognizer()

firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"

webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

with mic as source:
	r.adjust_for_ambient_noise(source)
	audio = r.listen(source)

result = r.recognize_google(audio)
checkresult = result.lower()
if checkresult.find("youtube") != -1:
	webbrowser.get('firefox').open("youtube.com")
	engine.say("Youtube started")
	engine.runAndWait()
if checkresult.find("duckduckgo") != -1:
  webbrowser.get('firefox').open("duckduckgo.com")
