import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys
import pyaudio
import google.generativeai as genai 
import webbrowser
import pyautogui
import datetime

genai.configure(api_key="AIzaSyCZ8ooy2P2iYKaji425vFedeuPjtIHfuCc")

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 120)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use male voice


def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")    
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("🗣️ You said:", command)
    except sr.UnknownValueError:
        talk("Sorry!, I didn’t catch that.")
        return ""
    except sr.RequestError:
        talk("Network issue with Google service... Please check your connection.")
        return ""
    return command

def generate_text(prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(prompt)
    return response.text

def talk(text):
    print("🎙️ VENKY:", text)
    engine.say(text)
    engine.runAndWait() 

def run_venky():
    command = take_command()

    if "play" in command:
        song = command.replace("play", "")
        talk("Playing  on YouTube 🎶")
        pywhatkit.playonyt(song)

    elif "date" in command:
        date = datetime.datetime.now().strftime('%A, %B %d, %Y')
        talk(f"It’s {date} ")

    elif "time" in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        talk(f"It’s {time} ")   


    elif "who is venkat" in command:
        info = (
            "Venkat is a graduate in Raghu Institute Of Technology "
            "He is a guy interested in entrepreneurship"
        )
        talk(info)

    elif "who is" in command:
        # person = command.replace("who is", "").strip()
        try:
            info = generate_text(command)
            info.replace("#","").strip
            info.replace("*","").strip
            talk(info)
        except:
            talk("Sorry, I couldn’t find information about that person.")

    elif "joke" in command:
        try:
            joke = generate_text(command)
            talk(joke)
        except:
            talk("Sorry! I couldn't find any jokes")

    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome ")
            os.startfile(chrome_path)
        else:
            talk("Chrome path not found !!!")

    elif "open downloads" in command:
        myfiles_path = "C:\\Users\\venka\\Downloads"
        if os.path.exists(myfiles_path):
            talk("Opening Downloads ")
            os.startfile(myfiles_path)
        else:
            talk("Downloads path not found!!!")


    elif "open code" in command or "open vs code" in command:
        talk("Opening VS Code 💻")
        os.system("code")
    
    elif "open" in command:
        site_name = command.replace("open","").strip()
        webbrowser.open_new_tab(f"https://www.{site_name}.com")

    elif "screenshot" in command:
        filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        pyautogui.screenshot().save(filename)
        talk("Screenshot taken")    

    elif "search" in command:
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        talk(f"Searching in Google for {query}")
       
    elif "exit" in command or "stop" in command or "bye" in command:
        talk("Okay Venky, see you later ")
        sys.exit()

    elif command != "":
        try:
            content = generate_text(command)
            content.replace("#","").strip()
            content.replace("*","").strip()
            talk(content)
        except:
             talk("I heard you, but I don’t understand that yet !")

talk("Yo! I'm venky – your personal voice assistant ")
while True: 
    run_venky()