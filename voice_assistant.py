import os
import pyttsx3
import speech_recognition as sr

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

# Function to Speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to Take Voice Input
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language="en-in")
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand. Please try again.")
            return "None"
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
            return "None"

# Function to Open Applications
def open_app(app_name):
    try:
        if "chrome" in app_name:
            speak("Opening Chrome")
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")  # Update path if needed
        elif "notepad" in app_name:
            speak("Opening Notepad")
            os.system("notepad.exe")
        elif "music" in app_name:
            speak("Playing music")
            os.startfile("C:\\path\\to\\your\\music.mp3")  # Update path to your music file
        else:
            speak("Sorry, I don't know how to open that.")
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I couldn't complete the task.")

# Main Loop
if __name__ == "__main__":
    speak("Hello JB, I am your voice assistant. How can I help you?")
    while True:
        command = take_command()

        if "open" in command:
            if "chrome" in command:
                open_app("chrome")
            elif "notepad" in command:
                open_app("notepad")
            elif "music" in command:
                open_app("music")
        elif "exit" in command or "stop" in command:
            speak("Goodbye JB! Have a great day.")
            break
        else:
            speak("Sorry, I didn't understand that. Please try again.")