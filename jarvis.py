import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
   engine.say(text)
   engine.runAndWait()   

# Test Jarvis voice
speak("Hello! I am Jarvis, your AI assistant.")


import speech_recognition as sr

def take_command():
    """Listens for a voice command and returns text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5) # Quick mic adjustment
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5) # Limit listening time 

    try:
        command = recognizer.recognize_google(audio).lower() # Directly return without extra print
        print(f"You said: {command}")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return None # Avoid unnecessary print
    except sr.RequestError:
        print("Speech recognition service unavailable.")
        return None

    return command

# Test voice input
command = take_command()
speak(f"You said: {command}") if command else speak("Try again!")



import datetime
import webbrowser
import wikipedia
import pywhatkit

def run_jarvis():
    """Processes voice commands smoothly"""
    command = take_command()
    if not command:
        return

    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "date" in command:
        date = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today's date is {date}")

    elif "weather" in command:
        webbrowser.open("https://www.google.com/search?q=weather")
        speak("Showing weather forecast")

    elif "search" in command:
        search_term = command.replace("search", "")
        webbrowser.open(f"https://www.google.com/search?q={search_term}")
        speak(f"Here are the search results for {search_term}")

    elif "location" in command:
        webbrowser.open("https://www.google.com/maps")
        speak("Opening Google Maps")

    elif "news" in command:
        webbrowser.open("https://news.google.com")
        speak("Here are some headlines")


    elif "who is" in command or "what is" in command:
        info = wikipedia.summary(command.replace("who is", "").replace("what is", ""), sentences=2)
        speak(info)

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")


    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "play" in command:
        song = command.replace("play", "")
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "quit jarvis" in command or "stop jarvis" in command:
        speak("Goodbye! Jarvis shutting down.")
        exit()  # Ends the program

    else:
        speak("Sorry, I didn't understand. Can you repeat?")


# Run Jarvis in a loop
while True:
    run_jarvis()


import tkinter as tk  # Import Tkinter for GUI

# Create main window
root = tk.Tk()
root.title("Jarvis AI Assistant")  # Window title
root.geometry("400x300")  # Set size
root.configure(bg="black")  # Background color

# Status Label
status_label = tk.Label(root, text="Jarvis is Ready", font=("Arial", 14), fg="white", bg="black")
status_label.pack(pady=20)

# Function to update status
def update_status(text):
    status_label.config(text=text)
    root.update()

# Modify speak() function to update GUI
def speak(text):
    update_status("Speaking...")
    engine.say(text)
    engine.runAndWait()
    update_status("Waiting for command...")

# Modify take_command() function to update GUI
def take_command():
    update_status("Listening...")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
    try:
        return recognizer.recognize_google(audio).lower()
    except:
        update_status("Could not understand. Try again.")
        return None

# Start Button
start_button = tk.Button(root, text="Start Jarvis", command=lambda: Thread(target=run_jarvis).start(), font=("Arial", 14))
start_button.pack(pady=20)

# Run GUI
root.mainloop()