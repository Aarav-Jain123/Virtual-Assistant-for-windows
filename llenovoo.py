import listentouser
import voicee
import weatherr
import os

if __name__ == "__main__":
    voicee.speak('Greetings user,')
    weatherr.greet_user()
    q = listentouser.takeCommand()
    if 'indigo' in q:
            print(f'Output: hello')
            voicee.speak(text="hello")
    elif 'open code' in q:
          os.startfile("C:\\Users\\Aarav Jain\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")