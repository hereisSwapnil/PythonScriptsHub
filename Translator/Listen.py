import speech_recognition as sr
from googletrans import Translator

#listen function
def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,6) #listening

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="hi")

    except:
        return ""
    
    query = str(query).lower()
    return query
#translate function
def TranslationHintoEng(text):
    line = str(text)
    translate = Translator()
    results = translate.translate(line,str = 'en')
    data = results.text
    print(f"You: {data}")
    return data
#connect
def Microcnnect():
    query = Listen()
    data = TranslationHintoEng(query)
    return data
Microcnnect()