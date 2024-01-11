import speech_recognition as sr
import pyaudio
import voicee


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source=source, phrase_time_limit=20) # phrase_time_limit
    try:
        print('Translating...')
        query = r.recognize_google(audio, language='en-in')
        print(f"{query}")
    except Exception as e:
        print("A problem has occured, please try again. We are trying our best to fix it.")
    return query
