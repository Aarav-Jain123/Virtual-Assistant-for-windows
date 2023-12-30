import listentouser
import voicee
import weatherr

if __name__ == "__main__":
    voicee.speak('Greetings user,')
    weatherr.greet_user()
    q = listentouser.takeCommand()
    if 'hello' in q:
            print(f'Output: hello')
            voicee.speak(text="hello")