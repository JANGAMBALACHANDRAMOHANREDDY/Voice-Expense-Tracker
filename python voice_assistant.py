import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I could not understand that.")
        return ""
    except sr.RequestError:
        print("Request failed, check your internet connection.")
        return ""

def run_voice_assistant():
    speak("How can I assist you?")
    command = take_command()
    
    if "open chrome" in command:
        speak("Opening Chrome")
        webbrowser.open("https://www.google.com")
    elif "search google" in command:
        speak("What should I search for?")
        search_query = take_command()
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    else:
        speak("Sorry, I don't recognize that command.")

if __name__ == "__main__":
    run_voice_assistant()
