import speech_recognition as sr

#Initialize recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Hello sir , Please Say Something")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said: " + text)
except Exception as e:
    print("Sorry, I could not understand the audio. Error: " + str(e))
