import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize text to speech
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("User said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

def main():
    speak("Hello, I am your personal voice assistant")

    while True:
        command = take_command()

        if "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {time}")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")

        elif "exit" in command or "stop" in command:
            speak("Goodbye")
            break

        elif command != "":
            speak("Command not recognized")

if __name__ == "__main__":
    main() 
