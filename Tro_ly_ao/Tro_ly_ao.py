import pyttsx3
import datetime 
import speech_recognition as sr
import webbrowser as wb
import os

Natus=pyttsx3.init()
voices = Natus.getProperty('voices')
Natus.setProperty('voice', voices[1].id) 

def speak(audio):
    print('Natus: ' + audio)
    Natus.say(audio)
    Natus.runAndWait()
   
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p") 
    speak("Dear boss, now is is:")
    speak(Time)

def welcome():
        #Chao hoi
        hour=datetime.datetime.now().hour
        if hour >= 6 and hour<10:
            speak("Good Morning Sir!")
        elif hour>=10 and hour<18:
            speak("Good Afternoon Sir!")
        elif hour>=18 and hour<24:
            speak("Good Evening sir")
        speak("How can I help you,boss") 

def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=1
        audio=c.listen(source)
    try:
        query = c.recognize_google(audio,language='en-US,vi')
        print("You want to: "+query)
    except sr.UnknownValueError:
        print('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Your order is: '))
    return query

def new_func(speak, command):
    search=command().lower()
    url = f"https://youtube.com/search?q={search}"
    wb.get().open(url)
    speak(f'Here is your {search} on youtube')

def main():
    
      while True:
        query=command().lower()
        #All the command will store in lower case for easy recognition
        if "google" in query:
            speak("What should I search,boss")
            search=command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        
        elif "youtube" in query:
            speak("What should I search,boss")
            search=command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
            
        elif"nhattruyen" in query:
            speak("What should I search,boss")
            url=f"http://www.nettruyen.com?q"
            wb.get().open(url)
            
        elif"email" in query:
            url=f"https://mail.google.com/mail/u/5/#inbox"
            wb.get().open(url)
            speak("What should I search,boss")
            
        elif "quit" in query:
            speak("Natus is off. Goodbye boss")
            quit()
            
        elif "open video" in query:
            video =r"C:\Users\ADMIN\Music\nhac\nhactre.mp4"
            os.startfile(video)
            
        elif 'time' in query:
            time()
            
if __name__  =="__main__":
    time()
    welcome()
    main()

  