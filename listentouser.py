import speech_recognition as sr


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source, phrase_time_limit=20) # phrase_time_limit
    try:
        print('Translating...')
        query = r.recognize_google(audio, language='en-us')
        print(query)
    except Exception as e:
        print('Say that again please...')