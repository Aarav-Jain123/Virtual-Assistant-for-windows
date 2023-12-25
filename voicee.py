# importing the pyttsx library 
import pyttsx3 
  
# initialisation 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# testing 
engine.say("My first code on text-to-speech") 
engine.say("Thank you, Geeksforgeeks") 
engine.runAndWait() 