import pyttsx3 as px
import speech_recognition as sr

rec = sr.Recognizer()
engine = px.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            speak('Listening...')
            voice = rec.listen(source, phrase_time_limit=2)
            command = rec.recognize_google(voice)
            command = command.lower()
            return command
    except:
        pass

def main():
    while True:
        command = takeCommand()
        if command is not None:
            speak('You might have said ' + command)
        else:
            speak('Please say something.')

main()