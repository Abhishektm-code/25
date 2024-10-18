import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import subprocess
import os


# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()
os.getcwd()

def cmd():

    # Listen for commands
    with sr.Microphone() as source:
        print("Clearing background noises... Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything...')
        engine.say('Ask me anything...')
        engine.runAndWait()
        recordedaudio = recognizer.listen(source)
        
    
    text = ""  # Initialize text variable
    try:
        text = recognizer.recognize_google(recordedaudio, language='en-US')
        text = text.lower()
        print('Your message:', text)

    except Exception as ex:
        print("Could not understand audio, please try again.")
        return  # Exit the function if there's an error
    
    if 'exit' in text:
        engine.say("Goodbye!")
        engine.runAndWait()
        return
    
    # Check commands
    if 'chrome' in text:
        a = 'Opening Chrome...'
        engine.say(a)
        engine.runAndWait()
        programName = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])
        
    if 'time' in text:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(current_time)
        engine.say(current_time)
        engine.runAndWait()
        
    if 'play' in text:
        a = 'Opening YouTube...'
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(text)
        webbrowser.open('https://www.youtube.com')
        
    if 'youtube' in text:
        b = 'Opening YouTube...'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://www.youtube.com')

    if "github" in text:
        c = 'opening github...'
        engine.say(c)
        engine.runAndWait()
        webbrowser.open("https://github.com")

    if 'whatsapp' in text:
        d = 'opening whatsapp...'
        engine.say(d)
        engine.runAndWait()
        webbrowser.open("https://whatsapp.com")
        
    if "ai" in text:
        e = 'opening chatgpt...'
        engine.say(e)
        engine.runAndWait()
        webbrowser.open("https://chatgpt.com")

    if "hackerrank" in text:
        f = 'opening hacker rank...'
        engine.say(f)
        engine.runAndWait()
        webbrowser.open("https://hackerrank.com")

    if "w3school" in text:
        g = 'opening w3school...'
        engine.say(g)
        engine.runAndWait()
        webbrowser.open("https://w3school.com")

    if 'code blocks' in text:
        a = 'Opening code blocks...'
        engine.say(a)
        engine.runAndWait()
        codeblocks_path = r"C:\Program Files\CodeBlocks\codeblocks.exe"
        subprocess.Popen([codeblocks_path])    

    
# Main loop
while True:
    cmd()
    