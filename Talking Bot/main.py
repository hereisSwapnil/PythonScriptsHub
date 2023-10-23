import pyttsx3
engine = pyttsx3.init()

call=input()
if call.lower()=="hi" or call.lower()=="hello" or call.lower()=="hey":
    engine.say("Hola")
    engine.runAndWait()
engine.say("What's your name my lady?")
engine.runAndWait()
print("What's your name? ")
usernm=input()
print("Hello "+usernm)
engine.say("Hello "+usernm)
engine.runAndWait()
engine.say("what are you doing?"+usernm)
engine.runAndWait()
