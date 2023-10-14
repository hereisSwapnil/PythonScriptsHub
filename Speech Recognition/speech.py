import os
import cv2
import smtplib
import pywhatkit
import pyttsx3 as px
import speech_recognition as sr
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
            voice = rec.listen(source, phrase_time_limit=2)
            command = rec.recognize_google(voice)
            command = command.lower()
            return command
    except:
        pass

def sendEmail(to, content, subject, email_add, email_pass):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        msg = MIMEMultipart()
        msg['From'] = email_add
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(content, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(email_add, email_pass)
        text = msg.as_string()
        server.sendmail(email_add, to, text)
        server.close()

def openChrome():
    os.system('start chrome')

def openNotepad():
    os.system('start notepad')

def openPaint():
    os.system('start mspaint')

def openWord():
    os.system('start winword')

def openExcel():
    os.system('start excel')

def openPowerpoint():
    os.system('start powerpnt')

def openCalculator():
    os.system('start calc')

def openCamera():
    os.system('start microsoft.windows.camera:')

def openZoom():
    os.system('start zoommtg:')

def openWhatsapp():
    os.system('start whatsapp:')

def capture():
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()

def main():
    speak('Hey there! I am your personal assistant. How can I help you?')
    while True:
        command = takeCommand()
        if command is not None:
            if 'play' in command:
                song = command.replace('play', '')
                speak('Playing' + song)
                pywhatkit.playonyt(song)
            elif 'send email' in command:
                try:
                    speak('What should I say?')
                    content = takeCommand()
                    speak('Who is the receiver?')
                    receiver = input('Enter receiver\'s email: ')
                    speak('What is the subject?')
                    subject = input('Enter subject: ')
                    speak('Enter your email address')
                    email_add = input('Enter your email address: ')
                    speak('Enter your email password')
                    email_pass = input('Enter your email password: ')
                    sendEmail(receiver, content, subject, email_add, email_pass)
                    speak('Email has been sent!')
                except Exception as e:
                    print(e)
                    speak('Unable to send email')
            elif 'capture' in command:
                capture()
            elif 'open chrome' in command:
                openChrome()
            elif 'open notepad' in command:
                openNotepad()
            elif 'open paint' in command:
                openPaint()
            elif 'open word' in command:
                openWord()
            elif 'open excel' in command:
                openExcel()
            elif 'open powerpoint' in command:
                openPowerpoint()
            elif 'open calculator' in command:
                openCalculator()
            elif 'open camera' in command:
                openCamera()
            elif 'open zoom' in command:
                openZoom()
            elif 'open whatsapp' in command:
                openWhatsapp()
            elif 'hello' in command or 'hi' in command:
                speak('Hey there!')
            elif 'who are you' in command:
                speak('I am your personal assistant.')
            elif 'stop' in command or 'quit' in command or 'bye' in command:
                speak('Okay Bye!')
                break
            else:
                speak('Please say the command again.')
            print(command)
        else:
            speak('Please say something.')

main()