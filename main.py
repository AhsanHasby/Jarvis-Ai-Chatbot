import speech_recognition as sr
import webbrowser
import pyttsx3
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    print(text)

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")


if __name__ == "__main__":
    speak("How can I help you?")
    while True: 
        try:
            with sr.Microphone() as source:
                print("Say...")
                recognizer.adjust_for_ambient_noise(source, duration = 1)
                audio = recognizer.listen(source, timeout = 5, phrase_time_limit = 5)
            
            word = recognizer.recognize_google(audio).lower()
            print(word)

            if "jarvis" in word: 
                speak("Order my owner")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")

                    recognizer.adjust_for_ambient_noise(source, duration = 1)
                    audio = recognizer.listen(source, timeout = 5, phrase_time_limit = 5)
                    command = recognizer.recognize_google(audio)

                    print("Me: ", command)
                    process_command(command)
                
        except Exception as e:
            print("Error; {0}".format(e))
            time.sleep(1)
 